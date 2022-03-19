secret  = 'westminster'
turns   = 6
guess   = ''
guesses = ''
missed  = 0
correct = False

print("Let's play Guess the Word")
print("You have 6 turns to guess the word!")
word = print("_ " * len(secret))
      
while turns > 0 :

    guess = input("\nGuess a letter :")
    guesses += guess
    
    for letter in secret :
        
        if letter in guesses:
            print("",letter,"",end="")
            correct = True
        else :
            print("_ ",end="")
            missed += 1
            if not correct:
                correct = False
                
    print()
    
    if missed == 0:
        break
    
    if not correct :
        turns -= 1

if missed != 0:
    print("End of Game.")    
else:
    print("You Won.")
    

                
    

            
                

    

