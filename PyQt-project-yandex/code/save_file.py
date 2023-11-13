import os

def save_file():
    os_name = os.name
    if os_name == "posix":
        os.system()
    elif os_name == "nt":
        os.system(r"explorer.exe c:\\")

if __name__ == "__main__":
    save_file()