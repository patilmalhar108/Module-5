def odd_even(n):
    if n ^ 1 == n + 1:
        return True
    else:
        return False
number = int(input("Enter your number: "))
if odd_even(number):
    print("Number is even")
else:
    print("Number is odd")