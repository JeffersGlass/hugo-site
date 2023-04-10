import csv
import json
import os

# PyScript server numbers
pyscript_guild = "972017612454232116"
rootpath = 'C:/Users/MSI1729/Downloads/discord_package_3_31_23/messages/'

# Get all folders
folders = [name for name in os.listdir(rootpath) if os.path.isdir(os.path.join(rootpath, name))]
channels: list[dict] = []

# Find all channels which belong to the PyScript 'Guild' (Server)
for folder in folders:
    with open(rootpath + folder + '/channel.json', 'r', encoding='utf-8') as fp:
        channel_preamble = json.load(fp)
        if 'guild' in channel_preamble and channel_preamble['guild']['id'] == pyscript_guild:
            channels.append({'id': channel_preamble['id'], 'name': channel_preamble['name']})

# Grab messages from Specific Channels
for channel in channels: 
    with open(rootpath + f'/c{channel["id"]}/messages.csv', 'r', encoding='utf-8') as fp:
        channel['lines'] = []
        reader = csv.DictReader(fp)
        for row in reader:
            channel['lines'].append(row)

# Print Number of Messages per Channel
for channel in reversed(sorted(channels, key=lambda c: len(c['lines']))):
    print(f"Channel {str(channel['name']): <40}{str(len(channel['lines'])): >10} messages")

# Total Messages
print(f"Total Messages: {sum(len(channel['lines']) for channel in channels) : >45} messages")