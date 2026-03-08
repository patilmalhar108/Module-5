def number_of_bits(n):
    count = 0
    while(n):
        count = count + 1
        n >>= 1
    return count

number = int(input("Enter your number: "))
print("Total bits is equal to:",number_of_bits(number))