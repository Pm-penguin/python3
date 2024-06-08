#PRAGYA MISHRA 0801IT22158
while True:
    try:
        number = float(input("Please enter a number greater than zero: "))
        assert number > 0, "Number must be greater than zero."
        break  
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except AssertionError as e:
        print(e)
        print("Please try again.")
print("You entered:", number)
