import random
cn = random.randint(1, 100)

print("--------------------------------------------------------------")
print("             WELCOME TO GUESS MY NUMBER GAME                  ")
print("The computer has chosen a number, you have to guess it!       ")
print("Maximum trials = 10                                           ")
print("--------------------------------------------------------------")

trials = 0
while trials <= 10:
    un = int(input("Your guess ?? "))
    trials += 1
    if(un > cn):
        print("Guess lower")
    elif(un < cn):
        print("Guess higher")
    else:
        print("CONGRATULATIONS!!")
        break

print("--------------------------------------------------------------")
print("You have taken %d trials" % trials)

if(trials < 4):
    print("Excellent Playing!")
elif(4 <= trials < 7):
    print("Good playing")
elif(7 <= trials < 10):
    print("OK")
else:
    print("Better luck next time..")

print("Thank you!")
