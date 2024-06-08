def add(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers and returns the difference."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers and returns the product."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers and returns the quotient. Handles division by zero error."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

def get_operation_choice():
  """Prompts user for operation choice and validates input."""
  while True:
    operation = input("""
      Choose operation:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      Enter choice (1/2/3/4): """)
    if operation in ('1', '2', '3', '4'):
      return int(operation)
    else:
      print("Invalid input. Please choose a number between 1 and 4.")

def main():
  """Main function for the calculator program."""
  print("Welcome to the Simple Calculator!")

  # Get numbers from user
  while True:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")

  # Get operation choice from user
  operation = get_operation_choice()

  # Perform calculation based on choice
  result = None
  if operation == 1:
    result = add(num1, num2)
  elif operation == 2:
    result = subtract(num1, num2)
  elif operation == 3:
    result = multiply(num1, num2)
  elif operation == 4:
    result = divide(num1, num2)

  # Display result
  if result is not None:
    print(f"Result: {result}")
  else:
    print(result)  # Prints division by zero error message

if __name__ == "__main__":
  main()
