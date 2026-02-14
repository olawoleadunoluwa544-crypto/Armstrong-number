number=int(input("enter a number:  "))
def is_armstrong(num):
    digits=str(num)
    power=len(digits)
    total= sum(int(digit)**power for digit in digits)
    return total==num
if is_armstrong(number):
    print(f"{number} is an armstrong number")
else:    print(f"{number} is not an armstrong number")
