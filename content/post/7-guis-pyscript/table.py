from formula_parser import FormulaParser

class Spreadsheet():
    def __init__(self):
        self.data : dict[tuple, str] = dict()

    def set(self, location: tuple, value: str):
        self.data[location] = value
    
    def getRawValue(self, location: tuple):
        return self.data(location)

    def getRenderedValue(self, location: tuple):
        value = self.data[location] 
        try:
            if value and self.data[location][0] == "=":
                return FormulaParser.parse(value[1])
        except IndexError as err:
            pass #Location out of bounds

        try:
            _ = float(value)
            return float(value)
        except Exception as err:
            pass

        return value
