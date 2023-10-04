num1 = int(input("enter your first number:-  "))
num2 = int(input("enter your second number:-  "))

a = input("type what do you want:- ")

if a == "+":
  result = num1 + num2 

if a == "-":
  result = num1 - num2

if a == "*":
  result = num1 * num2 
  
if a == "/":
    result = num1 / num2

print(result)
