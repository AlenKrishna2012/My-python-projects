import random

def guess_the_number():
    print(" Welcome to Guess the Number!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input(" Guess a number between 1 and 100 (or type 'exit' to quit): ")
        if guess.lower() == 'exit':
            print(" Thanks for playing!")
            break
        
        try:
            guess = int(guess)
            attempts += 1
            if guess < number_to_guess:
                print(" Too low! Try again.")
            elif guess > number_to_guess:
                print(" Too high! Try again.")
            else:
                print(f" Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print(" Please enter a valid number.")

def rock_paper_scissors():
    print(" Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input(" Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print(" Thanks for playing!")
            break
        if user_choice not in choices:
            print(" Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f" Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(" It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            print(" You win!")
        else:
            print(" You lose!")

def text_adventure():
    print(" Welcome to the Text Adventure Game!")
    
    scenarios = [
        " You find yourself in a dark room. You can go left or right.",
        " You are in a forest. You can go north or south.",
        " You stand at the edge of a cliff. You can climb down or walk along the edge."
    ]
    
    outcomes = {
        "left": [
            " You encounter a friendly dragon who gives you treasure!",
            " You meet a wise old man who offers you advice.",
            " You find a hidden passage that leads to a treasure chest!"
        ],
        "right": [
            " You fall into a pit and lose the game.",
            " You discover a magical portal that takes you to another realm.",
            " You encounter a fierce troll who challenges you to a riddle."
        ],
        "north": [
            " You find a hidden village where the villagers welcome you.",
            " You stumble upon a wild animal that chases you away!",
            " You discover an ancient ruin filled with artifacts."
        ],
        "south": [
            " You find a peaceful lake where you can rest.",
            " You encounter bandits who try to steal your belongings!",
            " You discover a hidden cave filled with glowing crystals."
        ],
        "climb down": [
            " You safely reach the bottom and find a treasure chest!",
            " You encounter a snake that bites you! Game over.",
            " You find an underground city filled with friendly creatures."
        ],
        " walk along the edge": [
            " You see a beautiful landscape but lose your balance and fall! Game over.",
            " You find a narrow path leading to safety.",
            " You encounter an old explorer who tells you stories of adventure."
        ]
    }
    
    while True:
        scenario = random.choice(scenarios)
        print(scenario)        
        choice = input(" What do you want to do? (Type your action or 'exit' to quit): ").lower()
        if choice == 'exit':
            break
        
        if choice in outcomes:
            outcome = random.choice(outcomes[choice])
            print(outcome)
        else:
            print(" Invalid choice. Please try again.")

def main_menu():
    games = {
        '1': guess_the_number,
        '2': rock_paper_scissors,
        '3': text_adventure,
        '4': lambda: print("Thank you for playing!"),
    }

    while True:
        print("\n---3-in-1 Gaming Console ---")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Text Adventure")
        print("4. Exit")
        
        choice = input("Choose a game (1-3) or type '4' to exit: ")
        
        if choice in games:
            games[choice]()  # Call the selected game function
            if choice == '4':
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
