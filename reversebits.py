number = int(input("Enter a number: "))
binary = bin(number) [2:]
reversed_binary = binary[::-1]
new_number = int(reversed_binary, 2)
print("Original binary is =",binary,"\n Reverse binary is =",reversed_binary,"\n New number is =",new_number)