def number_of_bits(n):
    ones = 0
    zero = 0
    while(n):
        if (n & 1 == 1):
            ones = ones + 1
        else:
            zero = zero + 1
        n >>= 1
    print("The number of ones is =",ones,"\nThe number of zeros is =",zero)

number = int(input("Enter your number: "))
number_of_bits(number)