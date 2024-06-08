#PRAGYA MISHRA 0801IT22158
List = [2, 58, 95, 999, 65, 32, 15, 1, 7, 45]
n = int(input("Enter the number to be searched: "))
found = 0 
for x in List:
    if x == n: 
        print("Item found at the Position:", List.index(n) + 1)
        found = 1
if found == 0:
    print("Item not found in list")
