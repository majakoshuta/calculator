while True:
    try:
        operationInput = input("Will you do addition, subtraction, multiplication, or division? ")
        if operationInput == "addition" or operationInput == "+":
            firstNumber = input("Give me the first number: ")
            secondNumber = input("Give me the second number: ")
            solution = int(firstNumber) + int(secondNumber)
            print("Your answer is " + str(solution) + "!")
        elif operationInput == "subtraction" or operationInput == "-":
            firstNumber = input("Give me the first number: ")
            secondNumber = input("Give me the second number: ")
            solution = int(firstNumber) - int(secondNumber)
            print("Your answer is " + str(solution) + "!")
        elif operationInput == "multiplication" or operationInput == "*":
            firstNumber = int(input("Give me the first number: "))
            secondNumber = int(input("Give me the second number: "))
            solution = firstNumber * secondNumber
            print("Your answer is " + str(solution) + "!")
        elif operationInput == "division" or operationInput == "/":
            firstNumber = input("Give me the first number: ")
            secondNumber = input("Give me the second number: ")
            solution = int(firstNumber) / int(secondNumber)
            print("Your answer is " + str(solution) + "!")
        elif operationInput == "exit":
            print("Goodbye!")
            break
        else:
            print("Choose from '+', '-', '*', and '/', please. Or type 'exit' to exit.")
    except ValueError:
        print("It has to be a number!")
    except ZeroDivisionError:
        print("You cannot divide by zero!")