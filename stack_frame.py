def main():
    a=10
    b=55
    print("in function main.......dir()=%s"%(dir()))
    result =absdiff(a,b)
    print("The absolute value of ",a,"-",b,"=",result)
def absdiff(x,y):
    print("in function absdiff......dir() =",dir())
    if x>y:
        z=x-y
    else:
        z=y-x
    return z
main()