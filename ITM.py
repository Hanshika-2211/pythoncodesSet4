# # What is your name ? Response should be 'User input' to ITM
# def user(name, department='ITM'):
#     return print('Hello,',name,'! Welcome to',department,'.')
# username = input("What is your name? ")
# response = user(username)
# print(response)
def myname(a,age,email):
    print('Hello,',a,'! Welcome to ITM Skills University.')
    print("Your details are:")
    print('Age:',age)
    print('Email Id:',email)
a=str(input("Enter the name:"))
age=int(input("Enter your age:"))
email=str(input("Enter your email:"))
myname(a,age,email)