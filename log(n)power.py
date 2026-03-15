print("Write a program to compute x ^ y")
def compute_power(x,y):
    result = 1
    while y > 0:
        if y % 2 == 0:
            x = x * x
            y >>= 1
        else:
            result = result * x
            y = y - 1
    return result

x = int(input("Enter the value of the number: "))
y = int(input("Enter the value of the power: "))
print("Total =",compute_power(x,y))