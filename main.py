import random
def main():
  # Create a list of options
  list1 = ["paper", "scissor", "rock"]

  # Verify user entry
  while True:
    # Input from user
    player1 = input("Please enter rock, paper, or scissor: ")
    if player1.lower() in list1:
        print("Entry accepted")
        game(player1, list1)
        break
    else:
        print("invalid entry")

# Play game function
def game(player1, list1):
    # computer chooses random choice from list
    player2 = random.choice(list1)
    print(f"computer chose {player2}")
    # compare user choice to computer choice
    if player1 == player2:
        print("Draw")
    elif player1 == "rock" and player2 == "paper":
        print(f"Player 1 loses")
    elif player1 =="rock" and player2 == "scissor":
        print("Player 1 wins")
    elif player1 == "paper" and player2 == "scissor":
        print("Player 1 loses")
    elif player1 =="paper" and player2 == "rock":
        print("Player 1 wins")
    elif player1 == "scissor" and player2 == "rock":
        print("Player 1 loses")
    elif player1 =="scissor" and player2 == "paper":
        print("Player 1 wins")

if __name__ == "__main__":
    main()