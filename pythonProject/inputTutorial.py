def is_float(value):
    if value is None:
        return False
    try:
        float(value)
        return True
    except:
        return False


# Calculator
calc = True
while calc:
    read = False
    while not read:
        value1 = input("Enter first number: ")
        value2 = input("Enter second number: ")

        if is_float(value1) & is_float(value2):
            number1 = float(value1)
            number2 = float(value2)
            read = True
        else:
            print("Those must be numbers!")
            read = False

    print("add:1, subtract:2, multiply:3, divide:4, exponent:5, root:6")

    result = 0
    success = False
    while not success:
        choice = int(input("What to do? "))

        if choice == 1:
            result = number1 + number2
            print(str(number1) + " + " + str(number2) + " = " + str(result))
            success = True
        elif choice == 2:
            result = number1 - number2
            print(str(number1) + " - " + str(number2) + " = " + str(result))
            success = True
        elif choice == 3:
            result = number1 * number2
            print(str(number1) + " * " + str(number2) + " = " + str(result))
            success = True
        elif choice == 4:
            result = number1 / number2
            print(str(number1) + " / " + str(number2) + " = " + str(result))
            success = True
        elif choice == 5:
            result = pow(number1, number2)
            print(str(number1) + " ^ " + str(number2) + " = " + str(result))
            success = True
        elif choice == 6:
            result = pow(number1, 1 / number2)
            print(str(number1) + " ^ 1/" + str(number2) + " = " + str(result))
            success = True
        else:
            print("Wrong choice, choose from 1 to 6.")
            success = False

    end = False
    while not end:
        goOn = input("Do you want to do another calculation? yes or no: ")
        if goOn == "yes":
            calc = True
            end = True
        elif goOn == "no":
            calc = False
            end = True
        else:
            end = False
