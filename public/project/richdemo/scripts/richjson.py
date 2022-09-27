from rich.json import JSON
from faker import Faker

fake = Faker()

data = fake.json(data_columns={'User':'name', 'ID':'pyint', 'Details':{'Favorite Color':'color_name', 'Address':'address'}}, num_rows=5)

print(JSON(data))