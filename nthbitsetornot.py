def set_or_not(number, n):
    if number & (1 << (n-1)):
        print("\nSet")
    else:
        print("\nNot Set")
    
number = int(input("Enter your number: "))
n = int(input("Enter the postition that you want to know if the bit the set or not: "))
set_or_not(number, n)