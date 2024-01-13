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
