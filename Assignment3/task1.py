def factorial(number):
    num = 1
    for i in range(1,number+1):
        num=num*i
    return num

user_input=int(input("Enter a number: "))
print(f"Factorial of {user_input} is: {factorial(user_input)}")



