#rock paper scissor
import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''____
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    
scissor='''
___________
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(rock)
print(scissor)
print(paper)

game_images=[rock,paper,scissor]
user_choice=int(input("what you choose? type 0 for rock , 1for paper,2 for scissor "))
print(game_images[user_choice])
computer_choice=random.randint(a=0,b=2)
print(f"computer chose:")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
   print("you typed wrong, you lose!")

if user_choice==0 and computer_choice==2:
    print("you wins!")
elif user_choice> computer_choice:
   print("you win!")
elif computer_choice > user_choice:
    print("you lose!")
elif computer_choice==user_choice:
 print("its a tie!")

  
