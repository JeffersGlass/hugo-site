from rich.table import Table
from faker import Faker

fake = Faker()

table = Table(title="Places")

table.add_column("Place", justify="left", style="bold", no_wrap=True)
table.add_column("Country Code", justify="left", style="", no_wrap=True)
table.add_column("Lat", justify="left", style="", no_wrap=True, width=7)
table.add_column("Lon", justify="left", style="", no_wrap=True, width=7)
table.add_column("Timezone", justify="left", style="", no_wrap=True)

for _ in range(5):
    lat, lon, place, country, tz = fake.location_on_land()
    table.add_row(place, country, lat, lon, tz)

print(table)