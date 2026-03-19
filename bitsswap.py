def swap1(a,b):
    print(a,b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping, a =",a)
    print("After swapping, b =",b)

def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + (~ b) + 1
    a = a + (~ b) + 1
    print("After swapping, a =",a)
    print("After swapping, b =",b)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
swap1(num1, num2)
swap2(num1, num2)