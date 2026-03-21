import math;
def print_power_set(set,setsize):
    power_setsize = int(math.pow(2,setsize));
    outer = 0;
    inner = 0;
    for outer in range(0,power_setsize):
        for inner in range(0,setsize):
            if ((outer & (1<<inner))> 0):
                print(set[inner], end = " ")
        print("")

size = int(input("Enter array size: "))
set = []
for i in range(0,size):
    n = int(input("Enter elements: "))
    set.append(n)
print_power_set(set,len(set))