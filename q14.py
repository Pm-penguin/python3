#PRAGYA MISHRA 0801IT22158
nterms = int(input("Enter no of terms:"))
n1, n2 = 0, 1
count = 0
if nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1