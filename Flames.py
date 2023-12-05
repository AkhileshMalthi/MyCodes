import time

def num_of_uncommons(name1, name2):
    """
    Returns the number of letters remaining after eliminating common letters between two names.
    """
    popped = []  # Store eliminated letters

    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i] == name2[j] and (j not in popped):
                print(f"{name1[:i]}[{name1[i]}] and {name2[:j]}[{name2[j]}]")
                popped.append(j)
                time.sleep(0.5)
                break

    remaining_letters = (len(name1) + len(name2)) - len(popped) * 2
    print(f"Total number of LETTERS REMAINING --> {remaining_letters}")
    return remaining_letters

def relation(steps):
    """
    Determines the relationship based on the number of steps.
    """
    flames = ["Friends", "Love", "Attraction", "Marriage", "Enemy", "Siblings"]
    ind = 0

    for i in range(5):
        ind = (ind + steps - 1) % (6 - i)
        flames.pop(ind)
    print(*flames)

def get_details():
    """
    Gets input for two names, removes spaces and chooses the smaller name as name1.
    """
    name1 = input("Enter First name: ").casefold()
    name1 = "".join(name1.split())

    name2 = input("Enter Second name: ").casefold()
    name2 = "".join(name2.split())

    if len(name1) > len(name2):
        name1, name2 = name2, name1
    return name1, name2

def result():
    """
    Gets details and calculates the relationship.
    """
    name1, name2 = get_details()
    relation(num_of_uncommons(name1, name2))

if __name__ == '__main__':
    result()
