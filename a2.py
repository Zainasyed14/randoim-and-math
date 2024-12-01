import random
playing = True
number = str(random.randint(10,100))
print("A number between 10 and 100 will be generated and you will have to guess it")
print("The game ends when you get 1!") 
while playing:
    guess= input("Give me your guess! \n")
    if number == guess:
        print("You win the game!!")
        print("The number was ", number)
        break
    elif number>guess:
        print("Guess a larger number")
    else:
        print("Guess a smaller number")