import random
print("Guess The Number Game", "\n")

num = int(input("1 to ...? "))
n = random.randint(1, num)
ch = int(input("How many chances you want? "))

if ch > num:
    print("Chances can not be higher than number")
    quit()

for i in range(0, ch):
    a = int(input("Enter your guess:"))
    if a == n:
        print("Your guess is correct")
        break
    elif a > num:
        print("Your guess can not be higher than number")
    else:
        print("Your guess is incorect")

print("The Number Was: ", n)
