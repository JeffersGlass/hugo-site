from formula_parser import FormulaParser, TokenType
from js import console

class Spreadsheet():
    def __init__(self):
        self.data : dict[tuple, str] = dict()

    def set(self, location: tuple, value: str):
        self.data[location] = value
    
    def getRawValue(self, location: tuple):
        return self.data[location]

    def getRenderedValue(self, location: tuple):
        value = self.data[location] 
        if value and self.data[location][0] == "=":
            tokens = FormulaParser.tokenize(value[1:])
            console.log(f"Tokens: {tokens}")
            if any([t.token_type == TokenType.T_CELL for t in tokens]):
                return FormulaParser.solve_with_references(tokens, self.data)
            else:
                return FormulaParser.solve_full_expression(tokens)
        else:
            return value
