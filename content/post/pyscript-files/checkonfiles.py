import os

print(f"Files in current working directory {os.getcwd()}:")
for file in os.listdir('.'):
    print("  " + file)