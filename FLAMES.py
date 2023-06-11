#A python program to get the FLAMES of two NAMES
def numofuncommons():
    num = len(name1+name2)
    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i]==name2[j]:
                num -= 2
                break
    return num

def result(steps):
    flames = ["Friends", "Love", "Attraction", "Marriage", "Enemy", "Siblings"]
    ind = 0
    for i in range(5):
        ind = (ind+steps-1)%(6-i)
        flames.pop(ind)
    print(*flames)

name1 = list(input("Enter First name: ").casefold())
while(" " in name1):
    name1.remove(" ")
name2 = list(input("Enter Second name: ").casefold())
while(" " in name1):
    name2.remove(" ")
result(numofuncommons())
