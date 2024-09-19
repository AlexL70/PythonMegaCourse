filenames = ('a.txt', 'b.txt', 'c.txt')
for name in filenames:
    file = open(name, 'r')
    content = file.read()
    file.close()
    print(content)