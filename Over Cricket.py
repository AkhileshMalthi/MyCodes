import random

def get_valid_input(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input not in range(1, 7):
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a valid number between 1 and 6.")

def play_innings(batting_player, bowling_player):
    scores = [1, 2, 3, 4, 6]
    score = 0

    for over in range(6):
        bowler = random.choice(scores)
        batsman = get_valid_input(f"{batting_player}, Hit --> ")

        if batsman == 5:
            batsman = 4
        elif batsman > 6:
            batsman = 6

        print(f"{bowling_player} delivered {bowler}")
        if bowler == batsman:
            print("OUT")
            break
        else:
            score += batsman
            print(f"Score: {score}".rjust(50))

    return score

def play_cricket():
    print("Welcome to OVER CRICKET GAME")
    player_name = input("Enter Your Name: ")

    overs_per_inning = int(input("Enter number of overs per inning: "))

    player_score = 0
    computer_score = 0

    for inning in range(1, 3):
        print(f"{inning}st Innings".center(50))
        print("-".center(50, "-"))
        print(f"\nBatting: {'Computer' if inning == 1 else player_name}\n"
              f"Bowling: {player_name if inning == 1 else 'Computer'}\n")
        print("-".center(50, "-"))

        if inning == 1:
            player_score = play_innings(player_name, "Computer")
            print(f"2nd Innings".center(50), f"\nTarget --> {player_score + 1}")
            print("-".center(50, "-"))
        else:
            computer_score = play_innings("Computer", player_name)

        print("-".center(50, "-"))
        print("Game Over".center(50))
        print(f"{player_name} Won".center(50) if player_score > computer_score else
              "Computer Won".center(50) if player_score < computer_score else "DRAW".center(50))
        print("-".center(50, "-"))

if __name__ == '__main__':
    play_cricket()
