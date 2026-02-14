# 1. PERSONAL INFORMATION FORMATTER
name=input("Enter your name: ")
age=int(input("Enter your age(in digits): "))
height=float(input("Enter your height(in feet): "))
print(f"Hello {name} , you are {age} years old and {height} feet tall.")

# SIMPLE ADDITION CALCULATOR
num_1=int(input("Enter the first number(as integer): "))
num_2=int(input("Enter the second number(as integer): "))
result=num_1+ num_2
print(f"The sum of{num_1} and {num_2} is {result}")

# STRING TO FLOAT CONVERTOR
price=input("Enter the price of the product(in digits): ")
price=float(price)
f_price=price+(price*(18/100))
print("The final price of the product after adding 18% GST is:",f_price)

# DATA TYPE CHECKER
i=24
s="Ram"
f=54.53
b=True
print(type(i),type(s),type(f),type(b))

# SECONDS TO MINUTES CONVERTOR
time=input("Enter time(in seconds): ")
time=int(time)
result=time/60
print(f"The {time} seconds in minutes is {result} minutes.")
