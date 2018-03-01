import random
answer=random.randint(1,100)
n=int(input("Please input num:"))
while n!=answer:
    if n > answer:
        n = int(input("Num is Big!Please Continue input: "))
    elif n < answer:
        n = int(input("Num is small!Please Continue input:"))

print("You win the game!")