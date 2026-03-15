def power_of_four(number):
    count = 0
    if (number & (~ (number & (number - 1)))):
        while number > 1:
            number >>= 1
            count = count + 1
        if count % 2 == 0:
            return True
        else:
            return False

number = int(input("Enter your number: "))
if power_of_four(number):
    print("Number is a power of 4")
else:
    print("Number is not a power of 4")