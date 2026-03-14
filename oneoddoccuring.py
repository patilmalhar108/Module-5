def odd_occuring(arr):
    res = 0
    for elemants in arr:
        res = res ^ elemants
    return res

arr = []
n = int(input("Enter the size of your array: "))
while(n):
    number = int(input("Enter number: "))
    arr.append(number)
    n = n - 1

print("Odd occuring number is:",odd_occuring(arr))