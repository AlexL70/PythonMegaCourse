def parse(feet_inches_param: str) -> (float, float):
    """ Parses string consisting of two numbers divided by space and returns these two numbers """
    parts = feet_inches_param.split(' ')
    feet_part = float(parts[0])
    inches_part = float(parts[1])
    return feet_part, inches_part


def convert(feet_part: float, inches_part: float) -> float:
    """ Convert feet and inches to meters """
    meters_part = feet_part * 0.3048 + inches_part * 0.0254
    return meters_part