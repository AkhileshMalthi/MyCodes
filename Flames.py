"""
        FLAMES PROGRAM BY AKHILESH MALTHI
"""
import time

# function which returns the number of letters remaining after common letters are eliminated
def numofuncommons(name1,name2): 

    popped = [] # to store the eliminated letters

    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i] == name2[j] and (j not in popped):
                print(f"{name1[:i]}[{name1[i]}] and {name2[:j]}[{name2[j]}]")
                popped.append(j)
                time.sleep(0.5)
                break

    rem = (len(name1)+len(name2))-len(popped)*2
    print(f"Total number of LETTERS REMAINING --> {rem}")
    return rem

def relation(steps):
    flames = ["Friends", "Love", "Attraction", "Marriage", "Enemy", "Siblings"]
    ind = 0

    for i in range(5):
        ind = (ind+steps-1)%(6-i)
        flames.pop(ind)
    print(*flames)

def result():
    relation(numofuncommons(name1,name2))

name1 = input("Enter First name: ").casefold()
name1 = "".join(name1.split())

name2 = input("Enter Second name: ").casefold()
name2 = "".join(name2.split())

# for faster result i will choose the smaller name as name1 and the otherone as name2
if len(name1) > len(name2):
    name1,name2 = name2,name1

if __name__ == '__main__':
    result();
