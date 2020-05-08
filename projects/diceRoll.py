import random

def main():
  num = random.randint(1, 6)

  print(num)

  print("The number is", num)

print(
  "Would you like to roll the dice again? (Please type yes or no only)")

x = input()

yes = "yes"

if (x == yes):
    main()

else :
  print("Thanks for playing")

return

main()
