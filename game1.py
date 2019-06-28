import random

number = random.randint(1,9)
#guess = input("Please enter a number: ")
count = 0
running = "true"

while running:
  guess = input("Please enter a number: ")
  if guess == "exit" or guess == "EXIT":
    print("You have chosen to exit.. Exiting!!")
    break
  elif int(guess) > number:
    print("You guessed too high")
  elif int(guess) < number:
    print("You guessed too low")
  elif int(guess) == number:
    print(f"Congrats! You guessed it correct and you took {count} tries for it. Well done")
    break
  count += 1
