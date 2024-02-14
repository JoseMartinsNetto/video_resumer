import os

def saveToFile(fileName: str, content: str) -> None:
    workdir = os.getcwd()
    
    with open(f'{workdir}/results/{fileName}', 'w') as file:
        file.write(content)

def getFileName(path: str) -> str:
    splited = path.split('/')

    return splited[-1].split('.')[0]

def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)

def readFromFile(fileName: str) -> str:
    workdir = os.getcwd()
    
    with open(f'{workdir}/results/{fileName}', 'r') as file:
        return file.read()

def print_header(title: str):
    count = len(title) + 6
    enclosingStr = ""

    for _ in range(count):
        enclosingStr += "="

    print(enclosingStr)
    print(f"== {title} ==")
    print(enclosingStr)