import string

for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    with open(file_name, "w") as f:
        f.write(file_name)