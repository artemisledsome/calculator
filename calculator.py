# calculator.py

def Add(x, y):
    return x+y 

def Subtract(x, y):
    return x-y

def Multiply(x, y):
    return x*y

def Divide(x, y):
    if y==0:
        return"taghsim bar sefr nadarim"
        return x/y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print("Result:", Add(num1, num2)) 
elif operation == '2':
    print("Result:", Subtract(num1, num2)) 
elif operation == '3':
    print("Result:", Multiply(num1, num2)) 
elif operation == '4':
    print("Result:", Divide(num1, num2))  
else:
    print("Invalid input")