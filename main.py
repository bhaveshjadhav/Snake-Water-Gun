import random


def cheeck(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1):
        return -1
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 0):
        return -1
    return 1


comp = random.randint(0, 2)
user = int(input("0 for snake,1 for water and -1 for gun:\n"))
print("You:", user)
print("Comp:", comp)
score = cheeck(comp, user)
if (score == 0):
    print("Its a draw")
elif (score == -1):
    print("lose")
else:
    print("won")
