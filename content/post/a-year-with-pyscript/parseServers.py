import json
import os


rootpath = 'C:\\Users\\MSI1729\\Downloads\\discord_package_3_31_23'
servers_folder_path = rootpath + '\\servers'

with open (servers_folder_path + '\\index.json', 'r') as f:
    data = json.load(f)

for key in data:
    print(f"{key: <25}{data[key]: <40}")