from rich.syntax import Syntax

syntax = Syntax.from_path('_richsetup.py', padding=1, line_range=(11, 20))
print(syntax)

raw_code = """@dataclass
class MailingAddress():
    name: str
    address: Sequence[str]

    @property
    def zipcode():
        return re.search('r\d{5}', self.address,) 
"""
print(Syntax(raw_code, "python", padding=1, theme="perldoc", line_numbers=True))