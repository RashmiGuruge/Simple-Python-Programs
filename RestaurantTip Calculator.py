#create variables
cost = 0
tip = 0

# Getting the user cost
cost = int(input("Enter the cost of your meal :Rs."))

# Displaying the Diners’satisfaction level
print ('''\n** Satisfaction levels **\n
   1).Totally satisfied
   2).Satisfied
   3).Dissatisfied\n''')

# Getting the satisfaction level 
level = int(input("Enter your satisfaction level :"))

#Getting conditions
if level == 1:
    tip = cost * (20/100)
    print('RS.',tip)
elif level == 2:
    tip = cost * (15/100)
    print('RS.',tip)
elif level == 3:
    tip = cost * (10/100)
    print('RS.',tip)
else:
    print("\n\t...Enter a proper satisfaction level...")
    

