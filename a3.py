import random
options=["Rock" , "Paper", "Scissors"]
computer_choice = random.choice(options)
user_choice=input("Choose Rock, Paper or Scissors : ")
print("Your Choice : " , user_choice)
print("Computers Choice : ", computer_choice)
if user_choice==computer_choice:
    print("Its a tie!")
elif user_choice=="Rock" and computer_choice=="Scissors":
    print("User has won since rock beats scissors")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("User has won since paper beats rock")
elif user_choice=="Scissors" and computer_choice=="Paper":
    print("User has won since scissor cuts paper")
else:
    print("The computer has won")