'''#Caluculator
while True:
    d=[]
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = input("Enter an operation: ")
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    else:
        print("please select a valid operation")'''



'''import random
print("Welcome to Rock,Paper,Scissor game!")
while True:
    user_score=0
    computer_score=0
    choices = ["Rock", "Paper", "Scissor"]
    userchoice=input("Enter Rock or Paper or Scissor : ")
    computerchoice = random.choice(choices)
    print(f"You chose: {userchoice}")
    print(f"Computer chose: {computerchoice}")
    if(userchoice=="scissor" and computerchoice=="Paper"):
      print("userchoice is win")
      user_score+=1
    elif(userchoice=="scissor" and computerchoice=="Rock"):
      print("computerchoice is win")
      computer_score+=1
    elif(userchoice=="Paper" and computerchoice=="Rock"):
      print("userchoice is win")
      user_score+=1
    elif(userchoice=="Paper" and computerchoice=="scissor"):
      print("comuterchoice is win")
      computer_score+=1
    elif(userchoice=="Rock" and computerchoice=="Paper"):
      print("computerchoice is win")
      computer_score+=1
    elif(userchoice=="Rock" and computerchoice=="scissor"):
      print("userchoice is win")
      user_score+=1
    else:
      print("The game is tie")
    print(f"Your score is : {user_score}")
    print(f"computer score is: {computer_score}")
    if(user_score>computer_score):
      print("user is winner")
    else:
      print("computer is winner")
    print("Do you want play again ?")'''


import random

spc = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '?', '>', '<', '~', '|']
cap = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
sma = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

a = int(input("How many numbers do you want? "))
b = int(input("How many special characters do you want? "))
c = int(input("How many characters do you want? "))

pas = []

if a < 0 or b < 0 or c < 0:
    print("Please enter a valid length.")
else:
    for i in range(a):
        index = random.randint(0, len(num) - 1)
        pas.append(num[index])
    for i in range(b):
        index = random.randint(0, len(spc) - 1)
        pas.append(spc[index])
    for i in range(c):
        index = random.randint(0, len(cap) - 1)
        pas.append(cap[index])
    for i in range(a + b + c, 12):
        index = random.randint(0, len(sma) - 1)
        pas.append(sma[index])
    for i in range(len(pas)):
        j = random.randint(0, len(pas) - 1)
        pas[i], pas[j] = pas[j], pas[i]
    final_password = ''
    for char in pas:
        final_password += char

    print(f"Generated password: {final_password}")





