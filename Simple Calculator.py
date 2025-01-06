# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Main function to perform operations
def main():
    print("Welcome to the Simple Calculator!")
    
    # User input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("\nEnter the operation number (1/2/3/4): ")
    
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    main()
