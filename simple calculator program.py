#create variables
num_1 = 0
num_2 = 0

#Getting user inputs
num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))
operator = input("Enter an operator :")

#Getting conditions
if operator == "+":
    add = num_1 + num_2
    print("Addition is :",add)
    
elif operator == "-":
    subtraction = num_1 - num_2
    print("Subtraction is :",subtraction)
    
elif operator == "*":
    multiplication = num_1 * num_2
    print("Multiplication is :",multiplication)
    
elif operator == "/":
    if num_2 == 0:
        print("Error")
    else:
        division = num_1 / num_2
        print("Division is :",division)

else:
    print("\nEnter a proper computation symbol")
    

