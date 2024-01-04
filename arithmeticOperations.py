# Do all the arithmetic operations using functions in a siingle program.
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

def addition(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2 != 0:
      return num1/num2
    else:
        print("The division is not possible.")

print("Addition:",addition(num1, num2))
print("Subtraction:",subtract(num1, num2))
print("Multiplication:",multiply(num1, num2))
print("Division:",division(num1,num2))