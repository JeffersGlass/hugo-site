from copy import deepcopy
from enum import Enum, auto
import re
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
my_dear = {TokenType.T_MULT : lambda x,y: x*y, TokenType.T_DIVIDE: lambda x, y: x/y}
aunt_sally = {TokenType.T_PLUS: lambda x,y: x+y, TokenType.T_MINUS: lambda x, y: x - y}

def quiet_index(i: Iterable, obj):
    try:
        index = i.index(obj)
    except ValueError as err:
        return -1

    return index

class ParseError(Exception):
    pass

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
            elif match := re.match(FormulaParser.re_operators, value):
                token = Node(token_type=arithmetic[match.group()], value = match.group())
            elif match := re.match(FormulaParser.re_decimal, value):
                token = Node(TokenType.T_NUM, value=float(match.group()))
            else:
                raise Exception(f"No further tokens found in {value}")
            tokens.append(token)
            value = value[match.end():]
            
        tokens = [Node(token_type=TokenType.T_LEFTP, value = "start")] + tokens + [Node(token_type=TokenType.T_RIGHTP, value = "end")]
        return tokens

    def get_referenced_cells(token_list: list) -> list:
        return [node for node in token_list if isinstance(node, Node) and node.token_type == TokenType.T_CELL]

    def find_closest_parens(token_list:list) -> tuple:
        leftIndex = -1
        rightIndex = -1
        for i, token in enumerate(token_list):
            if token.token_type == TokenType.T_LEFTP:
                leftIndex = i
            elif token.token_type == TokenType.T_RIGHTP:
                if leftIndex >= 0:
                    return leftIndex, i
                    break
                else:
                    raise Exception ("Left and right parentheses do not match")
        
        return -1, -1

    #-----------------------------------------#

    def solve_full_expression(token_list:list) -> float:
        original_list = deepcopy(token_list)
        while any([t.token_type in parens_types for t in token_list]):
            left_p, right_p = FormulaParser.find_closest_parens(token_list)
            result = FormulaParser.evaluate_simple_expression(token_list[left_p+1:right_p])
            token_list = (token_list[:left_p] if left_p > 0 else []) + [result] + (token_list[right_p + 1:] if (right_p < len(token_list) - 1) else [])
            

        if len(token_list) == 1:
            return token_list[0].value
        
        raise ParseError(f"Failed to parse full expression {original_list}\nFinal tokens were {token_list}")


    def evaluate_simple_expression(token_list:list) -> Node:
        original_list = deepcopy(token_list)
        if len(token_list) == 1:
            return token_list[0]

        token_list = FormulaParser.evaluate_for_single_opset(token_list, my_dear)
        token_list = FormulaParser.evaluate_for_single_opset(token_list, aunt_sally)
        
        if len(token_list) == 1:
            return token_list[0]
        else: raise ParseError(f"Failed to parse simple expression {original_list}\nFinal tokens were {token_list}")

    def evaluate_for_single_opset(token_list:list, operators:dict) -> list:
        while any(ops_to_do := [t.token_type in operators for t in token_list]):
            op_location = ops_to_do.index(True)
            func = operators[token_list[op_location].token_type]

            result = func(token_list[op_location-1].value, token_list[op_location+1].value)
            new_node = Node(TokenType.T_NUM, value = result)

            token_list = (token_list[:op_location-1] if op_location > 1 else []) + [new_node] + (token_list[op_location + 2:] if op_location < len(token_list) - 2 else [])
        return token_list

    def tokenize_and_solve(expression:str) -> float:
        return FormulaParser.solve_full_expression(FormulaParser.tokenize(expression))

    def solve_with_references(token_list:list, data: dict, already_referenced:set = None) -> float:
        #Not yet implemented
        return FormulaParser.solve_full_expression(token_list)

        '''
        Psuedocode:

        Get list of all references in tokens
            if any of these area in our already-referenced set, we have a loop and cannot solve this. Bail!
        Recursively get the values of each of those cells.
            If the cell is a striaght numerical value, just get a node with that value
            If the cell is not a number or tokenizable, BAIL! #REF error
            Tokenize their destination
            If they have references, call this again with self added to the list of referenced cells
            If not, solve them normally with solve_full_expression
        solve_full_expression of this normal expression
        Return
        '''



if __name__ == "__main__":
    values = [
        "2 + 3",
        "2 * 3",
        "2 + 3 * 4",
        "2 * 3 + 4",
        "2 * (3 + 4)",
        "(2 * 3) + 4",
        "(2 + 3) * (4 + 5)"
    ]
    for v in values:
        print(f"{v} = {FormulaParser.tokenize_and_solve(v)}")
