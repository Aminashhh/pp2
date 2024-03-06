import os

path = input()

if not os.path.exists(path):
    print(f"{path} does not exist.")
    exit()

if not os.access(path, os.W_OK):
    print(f"You do not have permission to delete {path}.")
    exit()

os.remove(path)
print(f"{path} has been deleted.")