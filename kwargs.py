# Write a code to pass positional arguments as well as keyword based arguments using arbitrary passing arguments.
def kbfunc(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)
kbfunc(name = "ABC", age = 32)
def func(args,*kwargs):
    for i in args:
        print(i)
    for j,k in kwargs.items():
        print(j,":",k)
func(1,5,8,3,Name = "Hanshika", Roll = 34)