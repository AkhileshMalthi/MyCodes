import random

def play_cricket():
    # Greetings
    print("Welcome to OVER CRICKET GAME")

    # Setting defaults
    scores = [1, 2, 3, 4, 6]
    com_score = 0
    player_score = 0

    # Getting player details
    player_name = input("Enter Your Name: ")

    # 1st Innings Code
    print("1st Innings".center(50))
    print("-".center(50, "-"))
    print(f"\nBatting : {player_name}\nBowling : Computer\n")
    print("-".center(50, "-"))

    # Player's batting
    for i in range(6):
        com = random.choice(scores)
        player = int(input("Hit --> "))

        # Restricting the hits as per rules
        if player == 5:
            player = 4
        elif player > 6:
            player = 6

        print(f"Computer delivered for {com}")
        if com == player:
            print("OUT")
            break
        else:
            player_score += player
            print(f"Score: {player_score}".rjust(50))

    # 2nd Innings Code
    print("2nd Innings".center(50), f"\nTarget --> {player_score + 1}")
    print("-".center(50, "-"))
    print(f"\nBatting : Computer\nBowling : {player_name}\n")
    print("-".center(50, "-"))

    # Computer's batting
    for i in range(6):
        player = int(input("Hit --> "))
        com = random.choice(scores)
        if com == player:
            print("OUT")
            break
        elif com_score > player_score:
            break
        else:
            print(f"Computer HIT --> {com} <--")
            com_score += com
            print(f"Score: {com_score}".rjust(50))
            print(f"Need {player_score - com_score} to Win")

    # Game result
    print("-".center(50, "-"))
    print("Game Over".center(50))
    print(f"{player_name} Won".center(50) if player_score > com_score else
          "Computer Won".center(50) if player_score < com_score else "DRAW".center(50))
    print("-".center(50, "-"))

if __name__ == '__main__':
    play_cricket()
