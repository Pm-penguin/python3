#PRAGYA MISHRA 0801IT22158
def is_palindrome(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    if num_str == reversed_str:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
