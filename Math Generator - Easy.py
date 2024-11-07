import random

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    func = random.randint(1, 2)
    if func == 1:
        equation = num1, "+", num2
        answer = num1 + num2
    elif func == 2:
        equation = num1, "-", num2
        answer = num1 - num2
    print(equation)
    answerinput = int(input())
    if answerinput == answer:
        print("Correct!")
    else:
        print("Wrong!")