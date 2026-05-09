import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
score_board = 0
activate = "y"
while activate == "y":
    choice_list = [rock, paper, scissors]
    computer_choice = random.choice(choice_list)
    print("Welcome to rock paper scissors!")
    choice_rock_paper_scissors = int(input("Enter your choice (rock(0), paper(1), or scissors(2)): "))

    if choice_rock_paper_scissors == 0:
        print(f"You choose Rock:\n {choice_list[0]}")
        print(f"Computer choose:\n {computer_choice}")
        if computer_choice == choice_list[0]:
            print("This was a Tie!")
        elif computer_choice == choice_list[1]:
            print("This was a Loss!")
        else:
            print("This was a Win!")
            score_board += 1
    elif choice_rock_paper_scissors == 1:
        print(f"You choose Paper:\n {choice_list[1]}")
        print(f"Computer choose:\n {computer_choice}")
        if computer_choice == choice_list[0]:
            print("This was a Win!")
            score_board += 1
        elif computer_choice == choice_list[1]:
            print("This was a Tie!")
        else:
            print("This was a Loss!")
    elif choice_rock_paper_scissors == 2:
        print(f"You choose Scissors:\n {choice_list[2]}")
        print(f"Computer choose:\n {computer_choice}")
        if computer_choice == choice_list[0]:
            print("This was a Loss!")
        elif computer_choice == choice_list[1]:
            score_board += 1
            print("This was a Win!")
        else:
            print("This was a Tie!")
    else:
        print(f"Wrong choice! Try again!\n")
        continue
    print(f"Current sessions core! {score_board}")
    activate = input("Do you want to play again? (y/n): ").lower()
    if activate == "y":
        continue
    else:
        break