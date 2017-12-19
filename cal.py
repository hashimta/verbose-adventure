def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x, y):
  return x*y
def div(x, y):
  return x/y
  
print("Select operation.")
print("'add' for addition")
print("'sub' for subtraction")
print("'mul' for multiplication")
print("'div' for divition")
 
selection = input("Enter selection:")
 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
if selection == 'add':
   print(add(num1,num2))
 
elif selection == 'sub':
   print(sub(num1,num2))
 
elif selection == 'mul':
   print(mul(num1,num2))
 
elif selection == 'div':
   print(div(num1,num2))
else:
   print("Incorrect input")
