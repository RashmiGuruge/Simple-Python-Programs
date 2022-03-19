secret = 'westminster'
turns = 6
guess = ''

print("Let's play Guess the Word")
print("You have 6 turns to guess the word!\n")
guess = input("Enter a secret word :")

while guess != secret :
    turns -= 1
    if turns == 0:
        break

    print("Number of turns left :",turns,"\n")
    guess = input("Enter a secret word :")

if guess != secret :
    print("opps !!!")
else :
    print("Congratulations")
