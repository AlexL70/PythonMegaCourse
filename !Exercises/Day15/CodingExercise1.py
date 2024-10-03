import random as rnd

lower: int = int(input("Enter lower bound: "))
upper: int = int(input("Enter upper bound: "))
num = rnd.randint(lower, upper)
print(f"Your number is {num}.")

