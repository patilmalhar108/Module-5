def check_if_same(number1, number2):
    if (number1 ^ number2 != 0):
        print("The numbers are not equal")
    else:
        print("The numbers are equal")

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
check_if_same(number1, number2)