import random
print("welcom to the Rock, Paper, Scissors game : ")
hand_Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
hand_Paper = """
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
hand_Scissors = """
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
instructions = input ("Press Enter to continue or type (Help) for the rules help : ").lower()
if instructions:
    print("""            ***********RULES ************
        1) You choose and the computer chooses 
        2) Rock smashes Scissors -> Rock wins
        3) Scissors cut paper -> Scissors win
        4) Paper covers Rock -> Paper wins""")
choice = input("Enter your choice (Rock, Paper, Scissors) : ").capitalize()
X = ["Rock", "Paper", "Scissors"]
if choice not in X :
    print("Invalid choice. Please run the program again and choce Rock, Paper, or Scissors.")
else:
    if choice == "Rock":
        print(f"\nYou chose:\n{hand_Rock}")
    elif choice == "Paper":
        print(f"\nYou chose:\n{hand_Paper} ")
    else:
        print(f"\nYou chose:\n{hand_Scissors}")
my_random = random.choice(X)
if my_random == "Rock":
    print(f"\nComputer chose:\n{hand_Rock}")
elif my_random == "Paper":
    print(f"\nComputer chose:\n{hand_Paper}")
else:
    print(f"\nComputer chose:\n{hand_Scissors}")
if choice == my_random:
    print("It's a tie! ")
elif ((choice == "Rock" and my_random == "Scissors")
      or
      (choice == "Paper" and my_random == "Rock")
      or
      (choice == "Scissors" and my_random == "Paper")
):
     print(f"congratulation! you won! {choice} beats {my_random}")
else:
    print(f"You lose! {my_random} beats {choice}")