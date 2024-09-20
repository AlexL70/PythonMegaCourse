password = input("Enter new password: ")

if len(password) < 8 or len(list(filter(lambda d: d.isdigit(), password))) == 0\
        or len(list(filter(lambda l: l.islower(), password))) == 0\
        or len(list(filter(lambda l: l.isupper(), password))) == 0:
    print("This is the weak password!")
else:
    print("This is a strong password!")