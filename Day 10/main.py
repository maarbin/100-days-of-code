# Calculator
import art

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mult(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div
}


def calculator():
  
  print(art.logo)
  num1 = float(input("What's the first number?: "))
  
  for key in operations:
    print(key)
  
  operation_symbol = input("Pick an operation from the above: ")
  
  num2 = float(input("What's the second number?: "))
  
  chosen_function = operations[operation_symbol]
  answer = chosen_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  start = True
  
  while start:
    retry = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit: ")
    num1_1 = answer
    if retry == 'y':
      operation_symbol2 = input("Pick an operation: ")
      num2_1 = int(input("What's the second number?: "))
      chosen_function = operations[operation_symbol]
      answer = chosen_function(num1_1, num2_1)
      print(f"{num1_1} {operation_symbol2} {num2_1} = {answer}")
    elif retry == 'n':
      start = False
      calculator()
  
  
calculator()