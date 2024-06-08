#PRAGYA MISHRA 0801IT22158
def exponential(n, x):
	sum = 1.0
	for i in range(n, 0, -1):
		sum = 1 + x * sum / i
	print ("e^x =", sum)
n = 10
x=int(input("Enter the value to which e is to be raised:"))
exponential(n, x)
