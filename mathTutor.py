import string
import random
correctProblems = 0
name = input("Type in your name:")
print("Hello",name,". Here are some math problems:") # the user name has been put in and the problems will begin

randomNumber1 = random.randrange(1,10) # generating random numbers
randNum1 = int(randomNumber1)
randomNumber2 = random.randrange(1,10)
randNum2 = int(randomNumber2)
randomNumber3 = random.randrange(1,10)
randNum3 = int(randomNumber3)
randomNumber4 = random.randrange(1,10)
randNum4 = int(randomNumber4)
randomNumber5 = random.randrange(1,10)
randNum5 = int(randomNumber5)
randomNumber6 = random.randrange(1,10)
randNum6 = int(randomNumber6)
randomNumber7 = random.randrange(1,10)
randNum7 = int(randomNumber7)
randomNumber8 = random.randrange(1,10)
randNum8 = int(randomNumber8)
randomNumber9 = random.randrange(1,10)
randNum9 = int(randomNumber9)
randomNumber10 = random.randrange(1,10)
randNum10 = int(randomNumber10)

print(randomNumber1,"+",randomNumber2) # first math problem
answer1 = input("What is the answer?")
ans1 = int(answer1)
correct1 = randNum1 + randNum2
if ans1 == correct1:
    print("Correct!")
    correctProblems+=1
if ans1 != correct1:
    print("Wrong. The right answer is ",randNum1+randNum2)

print(randomNumber3,"-",randomNumber4) # second math problem
answer2 = input("What is the answer?")
ans2 = int(answer2)
correct2 = randNum3 - randNum4
if ans2 == correct2:
    print("Correct!")
    correctProblems+=1
if ans2 != correct2:
    print("Wrong. The right answer is ",randNum3-randNum4)

print(randomNumber5,"X",randomNumber6) # third math problem
answer3 = input("What is the answer?")
ans3 = int(answer3)
correct3 = randNum5 * randNum6
if ans3 == correct3:
    print("Correct!")
    correctProblems+=1
if ans3 != correct3:
    print("Wrong. The right answer is ",randNum5*randNum6)

print(randomNumber7,"X",randomNumber8) # fourth math problem
answer4 = input("What is the answer?")
ans4 = int(answer4)
correct4 = randNum7 * randNum8
if ans4 == correct4:
    print("Correct!")
    correctProblems+=1
if ans4 != correct4:
    print("Wrong. The right answer is ",randNum7*randNum8)

print(randomNumber9,"-",randomNumber10) # fifth math problem
answer5 = input("What is the answer?")
ans5 = int(answer5)
correct5 = randNum9 - randNum10
if ans5 == correct5:
    print("Correct!")
    correctProblems+=1
if ans5 != correct5:
    print("Wrong. The right answer is ",randNum9-randNum10)

print(randomNumber2,"+",randomNumber7) # sixth math problem
answer6 = input("What is the answer?")
ans6 = int(answer6)
correct6 = randNum2 + randNum7
if ans6 == correct6:
    print("Correct!")
    correctProblems+=1
if ans6 != correct6:
    print("Wrong. The right answer is ",randNum2+randNum7)

print(randomNumber4,"+",randomNumber9) # seventh math problem
answer7 = input("What is the answer?")
ans7 = int(answer7)
correct7 = randNum4 + randNum9
if ans7 == correct7:
    print("Correct!")
    correctProblems+=1
if ans7 != correct7:
    print("Wrong. The right answer is ",randNum4+randNum9)

print(randomNumber10,"X",randomNumber1) # eighth math problem
answer8 = input("What is the answer?")
ans8 = int(answer8)
correct8 = randNum10 * randNum1
if ans8 == correct8:
    print("Correct!")
    correctProblems+=1
if ans8 != correct8:
    print("Wrong. The right answer is ",randNum10*randNum1)

print(randomNumber2,"X",randomNumber5) # nineth math problem
answer9 = input("What is the answer?")
ans9 = int(answer9)
correct9 = randNum2 * randNum5
if ans9 == correct9:
    print("Correct!")
    correctProblems+=1
if ans9 != correct9:
    print("Wrong. The right answer is ",randNum2*randNum5)

print(randomNumber7,"-",randomNumber3) # tenth math problem
answer10 = input("What is the answer?")
ans10 = int(answer10)
correct10 = randNum7 - randNum3
if ans10 == correct10:
    print("Correct!")
    correctProblems+=1
if ans10 != correct10:
    print("Wrong. The right answer is ",randNum7-randNum3)

correct = int(correctProblems)
print("You answered",correct,"problems correctly!" ) # calculate right answers
