import random 

def diceRoll():
  num = random.randint(1,6)

  print("this program will randomly generate a number from a dice roll \n")

  print("the number is:",num)

  print("would you like to roll again (please type yes or no only please) \n")

  x = input()

  if(x == "yes"):
    print("\n")
    diceRoll()
  else:
    print("thanks for playing!\n")

diceRoll()
