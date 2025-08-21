with open("myfile.txt","r", encoding="utf-8") as f:
    content = f.read()
    print(">>> Reading the whole file at once:")
    print(content)

with open("myfile.txt","r", encoding="utf-8") as f:
    print("\n>>> Reading with readline()")
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline