print("Write a program to divide two numbers without using a divison operater")
def divide(divident1, diviser1):
    sign = (-1 if ((divident1 < 0) ^ (diviser1 < 0)) else 1);
    divident1 = abs(divident1);
    diviser1 = abs(diviser1);
    
    quoteint = 0
    temp = 0
    
    for i in range(31, -1, -1):
        if (temp + (diviser1 << i) <= divident1):
            temp = temp + diviser1 << i
            quoteint |= 1 << i
    if sign == -1:
        quoteint = -quoteint
    return quoteint

a = int(input("Enter value of a for a/b: "))
b = int(input("Enter value of b for a/b: "))
print("Resualt of a/b is:",divide(a,b))