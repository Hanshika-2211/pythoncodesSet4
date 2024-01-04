# Calculate the square,square root and cube.
number=int(input("Enter the number:"))
def square(number):
    return number*number
def square_root(number):
    return number**0.5
def cube(number):
   return number*number*number
print("Square:", square(number))
print("Square root:", square_root(number))
print("Cube:", cube(number))