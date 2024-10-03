import glob
myfiles = glob.glob("/home/alexl70/cmd/*.sh")

for file in myfiles:
    print(f"\n\nContent of {file}:\n")
    with open(file, 'r') as f:
        content = f.read()
        print(content)