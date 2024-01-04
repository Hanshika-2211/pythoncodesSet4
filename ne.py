# Take how many elements you require in the list, then get the user input for the same and form a list. Then get the list into the function
def add(*args):
    sum1=sum(args)
    return sum1
l=int(input("Enter number of arguements: "))
my_list=[]
for i in range(l):
    my_list.append(int(input(f"Enter value: ")))
print(*my_list)
print(add(*my_list))