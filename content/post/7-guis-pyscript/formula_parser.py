from enum import Enum, auto
from lib2to3.pgen2 import token
import re
from tokenize import Token

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

arithmetic = {
    "+" : TokenType.T_PLUS,
    "-" : TokenType.T_MINUS,
    "/" : TokenType.T_DIVIDE,
    "*" : TokenType.T_MULT,
    "(" : TokenType.T_LEFTP,
    ")" : TokenType.T_RIGHTP,
}


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = list()
    
    def __str__(self):
        return f"Node ({self.token_type}): {self.value}" + (f"children: {self.children}" if self.children else "")

    def __repr__(self):
        return self.__str__()

class FormulaParser():
    re_ident = r"[a-zA-Z_]\w*" #matches identifiers
    re_decimal = r"-?\d+(\.\d*)?" #matches decimal numbers
    re_cell = r"([a-zA-Z])(\d+)" #group 1 is column, group 2 is row
    re_range = re_cell + ":" + re_cell #matches a range like A2:B4
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
            
        tokens.append(Node(TokenType.T_END, "end"))
        return tokens

    def get_referenced_cells(token_list: list) -> list[str]:
        return [node for node in token_list if isinstance(node, Node) and node.token_type == TokenType.T_CELL]


if __name__ == "__main__":
    value = "3+ C4 / 7 + D2"
    result = FormulaParser.tokenize(value)
    references = FormulaParser.get_referenced_cells(result)
    for token in references:
        print(token)


        



