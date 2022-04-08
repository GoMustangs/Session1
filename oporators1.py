number1 = input("Enter your first number:")
realNumber1 = int(number1)
number2 = input("Enter your second number:")
realNumber2 = int(number2)
print("Here is what you get when you add your numbers together:", realNumber1+realNumber2)
print("Here is what's left when you subtract your second number from your first:", realNumber1-realNumber2)
print("Here is what you get when you multiply your numbers by eachother:", realNumber1*realNumber2)
if realNumber2 == 0:
    print("You cannot divide a number by zero.")
if realNumber2 > 0:
    print("Here is what you get when you divide your first number by your second number:", realNumber1/realNumber2)
    print("Here is the remainder from the first number divided by the second number:", realNumber1%realNumber2)
