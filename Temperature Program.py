# Create variable
choice = 0
temp = 0
fahrenheit = 0
celsius = 0

# Displaying options
print ("(1). Celsius to Fahrenheit")
print ("(2). Fahrenheit to Celsius\n")

# Getting user choice
choice = int(input("Enter your choice :"))

#Getting condition
if choice == 1:
    
    #Getting user input
    temp = int(input("\nEnter a temperature value:"))
    #converting Celsius to Fahrenheit
    fahrenheit = (temp * 1.8)+32
    #Print fahrenheit value
    print(fahrenheit,"F")
    
elif choice == 2:
    
    #Getting user input
    temp = int(input("\nEnter a temperature value:"))
    #converting Fahrenheit to Celsius  
    celsius = (temp - 32)/1.8
    #Print celsius value
    print(celsius,"C")
    
else:
    print("\n...invalid option entered...")
