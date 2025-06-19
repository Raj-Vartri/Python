import math
number = float(input("Enter a positive number: "))

if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
else:
    square_root = "Undefined (number must be positive)"
    natural_log = "Undefined (log not defined for zero or negative numbers)"

sine_value = math.sin(number) 


print("Square root : ",square_root)
print("Logarithm :",natural_log)
print("Sine :",sine_value)
