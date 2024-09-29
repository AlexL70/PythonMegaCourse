feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_param: str) -> (float, float, float):
    parts = feet_inches_param.split(' ')
    feet_part = float(parts[0])
    inches_part = float(parts[1])
    meters_part = feet_part * 0.3048 + inches_part * 0.0254
    return feet_part, inches_part, meters_part


(feet, inches, meters) = convert(feet_inches)
print(f"{feet} feet and {inches} inches equals to {meters} meters")
if meters < 1:
    print("Kid is too small.")
else:
    print("Well, kid can use a slide")