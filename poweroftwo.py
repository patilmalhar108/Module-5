def power_of_two(number):
    if number == 0:
        return 0
    if (number & (~ (number - 1))) == number:
        return 1
    return 0

number = int(input("Enter your number: "))
if power_of_two(number):
    print("\n The number is power of 2")
else:
    print("The number is not power of 2")