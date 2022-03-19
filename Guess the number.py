import random

hidden = random.randrange(1,20)

for i in range(5):
     
     guess = int(input("Please input a number between 0 and 100:"))
     
     if (hidden != guess) :
          if guess > hidden:
               print ("Your guess is too low")
          else :
               print ("Your guess is too high")      
     else:
          print("You got it in.This is the correct number.")
          break
     
print("\nThe correct answer was",hidden)
