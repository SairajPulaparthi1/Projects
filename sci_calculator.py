#SairajPulaparthi
#Lab 3 Sci Calculator

import math
#start defining the variables
result= 0.0
print("Current Result:", result )
numValue = 0.0
numCalc = 0
print("Calculator Menu")
print("---------------")
print("0. Exit Program")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Logarithm")
print("7. Display Average")
print("")
print("")
print("")
print("")
menu= int(input(f"Enter Menu Selection:"))
print("")
#start the while function
while (menu != 0 or menu == 0 or menu <=7):

#this is for out of bound selection
    if menu < 0 or menu > 7:
        print("Error: Invalid selection!")

        menu = float(input(f"Enter Menu Selection:"))
        print("Thanks for using this calculator. Goodbye!")
        break

    elif menu == 0:

        print("Thanks for using this calculator. Goodbye!")
        break

#the start of the calcutor 1-6 processes
    elif menu == 1:

        first_operand = float(input(f"Enter first operand: "))
        second_operand = float(input(f"Enter second operand: "))
        result = float(first_operand + second_operand)
        numValue += result
        numCalc += 1
        print('Current Result:', result)
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        menu = int(input("Enter Menu Selection:"))

    elif menu == 2:

        first_operand = float(input(f"Enter first operand: "))
        second_operand = float(input(f"Enter second operand: "))
        result = (first_operand - second_operand)
        numValue += result
        numCalc += 1
        print('Current Result:', result)

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        menu = int(input("Enter Menu Selection:"))



    elif menu == 3:

        first_operand = float(input(f"Enter first operand: "))
        second_operand = float(input(f"Enter second operand: "))
        result = (first_operand * second_operand)
        numValue += result
        numCalc += 1
        print(f'Current Result:{result:.2f}')

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        menu = int(input("Enter Menu Selection:"))

    elif menu == 4:
        first_operand = float(input(f"Enter first operand: "))
        second_operand = float(input(f"Enter second operand: "))
        result = float(first_operand / second_operand)
        numValue += result
        numCalc += 1
        print(f'Current Result:{result:.2f}')

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        menu = int(input("Enter Menu Selection:"))

    elif menu == 5:
        first_operand = float(input(f"Enter first operand: "))
        second_operand = float(input(f"Enter second operand: "))
        result = math.pow(first_operand, second_operand)
        numValue += result
        numCalc += 1
        print(f'Current Result:{result:.2f}')

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        menu = int(input("Enter Menu Selection:"))

    elif menu == 6:
        first_operand = float(input(f"Enter first operand: "))
        second_operand = float(input(f"Enter second operand: "))
        result = math.log(second_operand, first_operand)
        numValue += result
        numCalc += 1
        print(f'Current Result:{result:.1f}')

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        menu = int(input("Enter Menu Selection:"))
# the start of the 7 function
    elif menu == 7:
        if numValue == 0:
            print("Error: No calculations yet to average!")
            print("Enter Menu Selection: ")
            print("Thanks for using this calculator. Goodbye!")
            break
        else:
            average = numValue/numCalc
            print("Sum of calculations: ", numValue)
            print("Number of calculations: ", numCalc)
            print(f'Average of calculations:{average:.2f}')
            print("Enter Menu Selection: ")
            print("Thanks for using this calculator. Goodbye!")

            break




