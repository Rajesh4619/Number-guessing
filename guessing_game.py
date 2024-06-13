import random

number = random.randint(1, 100)

player_name = input("Hi, What is your name? ")
number_of_guesses = 0

print(f"Alright {player_name}! I am thinking a number between 1 and 100:")
print(f"Try in guess it in 10 tries")
while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print(f"Congratulations,{player_name}! You guessed the number in  {number_of_guesses}  tries!")
else:
    print(f"Sorry,{player_name}, you did not guess the number. The number was {number}")
