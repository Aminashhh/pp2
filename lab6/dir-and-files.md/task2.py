import os

def access(path):
    if os.path.exists(path):
        print(f"{path} is exist")
    else:
        print(f"{path} is gone")
    if os.access(path, os.R_OK):
        print(f"{path} is readability")
    else:
        print(f"{path} is not readability")
    if os.access(path, os.W_OK):
        print(f"{path} is writability")
    else:
        print(f"{path} is not writability")
    if os.access(path, os.X_OK):
        print(f"{path} is executability")
    else:
        print(f"{path} is not executability")

pp=os.path.join(os.getcwd(), "lab6")
pp1=os.path.join(os.getcwd(), r"C:\Users\user\Desktop\PP2\lab6\lab6/dir-and-files.md")
access(pp)
access(pp1)