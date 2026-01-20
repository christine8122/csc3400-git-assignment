# main.py
from calculator import add, subtract, multiply, divide

def display_menu():
    """Display the calculator menu."""
    print("\n=== Command-Line Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 32)

def get_numbers():
    """Get two numbers from user input."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None

def main():
    """Main calculator loop."""
    while True:
        display_menu()
        choice = input("Select operation (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue
        
        a, b = get_numbers()
        if a is None or b is None:
            continue
        
        try:
            if choice == '1':
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"Result: {a} × {b} = {result}")
            elif choice == '4':
                result = divide(a, b)
                print(f"Result: {a} ÷ {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()