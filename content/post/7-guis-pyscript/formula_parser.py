from enum import Enum, auto
import re
from math import prod
from typing import Iterable

class TokenType(Enum):
    T_NUM = auto()
    T_EMPTY = auto()
    T_PLUS = auto()
    T_MINUS = auto()
    T_DIVIDE = auto()
    T_MULT = auto()
    T_LEFTP = auto()
    T_RIGHTP = auto()
    T_CELL = auto()
    T_END = auto()
    T_EXPRESSION = auto()

arithmetic = {
    "+" : TokenType.T_PLUS,
    "-" : TokenType.T_MINUS,
    "/" : TokenType.T_DIVIDE,
    "*" : TokenType.T_MULT,
    "(" : TokenType.T_LEFTP,
    ")" : TokenType.T_RIGHTP,
}

parens_types = {TokenType.T_LEFTP, TokenType.T_RIGHTP}
my_dear = {TokenType.T_MULT : prod, TokenType.T_DIVIDE: lambda x, y: x/y}
aunt_sally = {TokenType.T_PLUS: sum, TokenType.T_MINUS: lambda x, y: x - y}

def quiet_index(i: Iterable, obj):
    try:
        index = i.index(obj)
    except ValueError as err:
        return -1

    return index

class Node:
    def __init__(self, token_type, value=None, children=None):
        self.token_type = token_type
        self.value = value
        if children == None: self.children = list()
        else: self.children = children
    
    def __str__(self):
        return f"Node ({self.token_type}):'{self.value}'" + (f" children: {self.children}" if self.children else "")

    def __repr__(self):
        return self.__str__()

    def get_value(self):
        if self.token_type == TokenType.T_NUM:
            return float(self.value)
        else: raise Exception(f"Could not derive value of token {self}")

class FormulaParser():
    #re_ident = r"[a-zA-Z_]\w*" #matches identifiers
    re_decimal = r"-?\d+(\.\d*)?" #matches decimal numbers
    re_cell = r"([a-zA-Z])(\d+)" #group 1 is column, group 2 is row
    #re_range = re_cell + ":" + re_cell #matches a range like A2:B4
    re_operators = r'[\+\-\/\*\(\)]'

    @staticmethod
    def tokenize(value: str):
        if not value or len(value) <= 0: return
        value = ''.join(value.split()) #remove all whitespace

        tokens = list()
        while len(value) > 0:
            token = None
            match = None
            if match := re.match(FormulaParser.re_cell, value):
                token = Node(TokenType.T_CELL, value=match.group())
            elif match := re.match(FormulaParser.re_decimal, value):
                token = Node(TokenType.T_NUM, value=match.group())
            elif match := re.match(FormulaParser.re_operators, value):
                token = Node(token_type=arithmetic[match.group()], value = match.group())
            else:
                raise Exception(f"No further tokens found in {value}")
            tokens.append(token)
            value = value[match.end():]
            
        tokens = [Node]
        tokens.append(Node(TokenType.T_END, "end"))
        return tokens

    @staticmethod
    def get_referenced_cells(token_list: list) -> list:
        return [node for node in token_list if isinstance(node, Node) and node.token_type == TokenType.T_CELL]

    @staticmethod
    def evaluate_parenfree_expression(token_list:list):
        if len(token_list) == 1:
            return token_list[0].get_value()
        else:
            pass

    @staticmethod
    def evaluate(token_list:list, operators:dict) -> float:
        
        if not any([t.token_type == op for t in token_list for op in operators]):
            print(f"No operators found in {token_list} from list {operators}")
            return token_list

        for t_type, func in operators.items():
            while index:= quiet_index([t.token_type for t in token_list], t_type) >= 0:
                result = func(token_list[index-1].get_value(), token_list[index+1].get_value())
                new_node = Node(TokenType.T_NUM, value=result)
                token_list = FormulaParser.evaluate(token_list[:max(0,index-2)] + [new_node,] + token_list[min(len(token_list), index+2):], operators)
        
        return token_list

    def find_closest_parens(token_list:list) -> tuple:
        leftIndex = -1
        rightIndex = -1
        for i, token in enumerate(token_list):
            if type(token) == list:
                print(token_list)
                print(token)
            if token.token_type == TokenType.T_LEFTP:
                leftIndex = i
            elif token.token_type == TokenType.T_RIGHTP:
                if leftIndex >= 0:
                    return leftIndex, i
                    break
                else:
                    raise Exception ("Too many right-parentheses")
        
        return -1, -1


    def handle_parens(token_list: list, leftIndex, rightIndex, operators) -> list:
        print(f"Evaluating {token_list} with operators {operators.keys()}")
        exp = FormulaParser.evaluate(token_list[leftIndex+1:rightIndex], operators)
        new_list = token_list[:leftIndex] + exp + token_list[rightIndex+1:]
        return new_list

    def handle_all_parens(token_list:list) -> list:
        while FormulaParser.find_closest_parens(token_list) != (-1, -1): #any([t.token_type in parens_types for t in token_list]):
            left, right = FormulaParser.find_closest_parens(token_list)
            token_list = FormulaParser.handle_parens(token_list, left, right, my_dear)
            token_list = FormulaParser.handle_parens(token_list, left, right, aunt_sally)
        return token_list


if __name__ == "__main__":
    value = "(3/4) + 1"
    result = FormulaParser.tokenize(value)
    for r in result:
        print(r)
    print("----")

    result = FormulaParser.handle_all_parens(result)
    for r in result:
        print(r)
    print("----")
