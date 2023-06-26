import random

print("1 - Dice Roll", "2 - Exit", sep=" ")

a = int(input(": "))
if a == 1:
    b = random.randint(1, 6)
    print(b)
else:
    quit()
