def print_two_odd(arr, size):
    xor_of_two = arr[0]
    x = 0
    y = 0
    setbit = 0
    for i in range(1, size):
        xor_of_two = xor_of_two ^ arr[i]
    setbit = xor_of_two & ~(xor_of_two - 1)
    for i in range(size):
        if (arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print("The two odd elemants are:",x,"and",y)
    
arr = []
arrsize = int(input("Enter size of the array: "))
for i in range(0,arrsize):
    z = int(input("Enter the elemants: "))
    arr.append(z)

print_two_odd(arr, arrsize)