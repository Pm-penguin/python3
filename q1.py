#PRAGYA MISHRA 0801IT22158
def frequency(num_list, target):
    f = 0
    for num in num_list:
        if num == target:
            f += 1
    return f
Num_list = [1,2,1,2,4,2,5,7,5,8,6,9,5,5,4,1,26,5,21,6,5,21,6,5,2,1,7,41,3,6,25,74]
target = int(input("Enter the number to find its frequency: "))
freq = frequency(Num_list, target)
print("Frequency of", target, ":", freq)
