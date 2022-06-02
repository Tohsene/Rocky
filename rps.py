import random
print("Welcome to my Rock Paper Scissors game. Sit back and enjoy!")
print("R for rock, P for paper, S for scissors")

while True:
    choices = ["R", "P", "S"]

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        player = input("R, P or S?: ")

    if player==CPU:
        print(f"Player({player}):CPU({CPU})")
        print("Tie!")
    elif player=="R":
        if CPU == "P":
            print(f"Player({player}):CPU({CPU})")
            print("You lose!")
        if CPU == "S":
            print(f"Player({player}):CPU({CPU})")
            print("You win!")
    elif player=="S":
        if CPU == "R":
            print(f"Player({player}):CPU({CPU})")
            print("You lose!")
        if CPU == "P":
            print(f"Player({player}):CPU({CPU})")
            print("You win!")
    elif player=="P":
        if CPU == "S":
            print(f"Player({player}):CPU({CPU})")
            print("You lose!")
        if CPU == "R":
            print(f"Player({player}):CPU({CPU})")
            print("You win!")
    play_more = input("Play again? (yes/no): ").lower()
    if play_more != "yes":
        break
print("Goodbye!")