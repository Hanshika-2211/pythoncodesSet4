# # Explanation code 1:
# def my_function():
#      print("Hello students")
# my_function()

# # Explanation code 2:
# def my_function(*args):
#     for i in args:
#         print(i)
# my_function(3)
# my_function(3,4)
# my_function(3,4,5)

# # Explaination code 3:
# def my_function(a,b,*args):
#     print(a)
#     print(args)
# my_function(1,2,3,4,5)

# # Explaination code 4:
# def kbfunction(**kwargs):
#     print(kwargs)
# kbfunction(name='ABC',age=32)

# # Explaination code 5:
# var_global=4
# def function():
#     global var_global
#     var_global=3
#     print(var_global)
# function()

# Explaination code 6:
var1=10
def func():
    var1=3
    print(var1)
    def funct2():
        nonlocal var1
        var1=4
        print(var1)
    funct2()
    print(var1)
func()
print(var1)