from faker import Faker

from rich.columns import Columns
from rich.text import Text

fake = Faker()
users = (Text(t) for t in sorted((fake.file_name(category="text") for _ in range(50)), key=str.upper))

print("Here are 50 file names, nicely arranged into [b]Columns[/b]:")
print(Columns(users))

