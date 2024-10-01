from parse_and_convert14 import parse, convert

feet_inches = input("Enter feet and inches: ")

(feet, inches) = parse(feet_inches)
meters = convert(feet, inches)
print(f"{feet} feet and {inches} inches equals to {meters} meters")
if meters < 1:
    print("Kid is too small.")
else:
    print("Well, kid can use a slide")