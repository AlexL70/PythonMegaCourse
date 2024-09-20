try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("We do not accept squares. Sorry.")

    area = width * length
    print(area)
except ValueError:
    print("Please enter valid numbers")