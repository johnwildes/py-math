# filepath: math-helper-app/math-helper-app/src/main.py

def main():
    print("Welcome to the Math Helper App!")
    print("Select a type of math problem to solve:")
    print("1. Arithmetic")
    print("2. Geometry")
    print("3. Fractions")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            import modules.arithmetic as arithmetic
            arithmetic_menu()
        elif choice == '2':
            import modules.geometry as geometry
            geometry_menu()
        elif choice == '3':
            import modules.fractions as fractions
            fractions_menu()
        elif choice == '4':
            print("Thank you for using the Math Helper App! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def arithmetic_menu():
    print("Arithmetic Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Back to main menu")

    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                print("Result:", arithmetic.add(num1, num2))
            elif choice == '2':
                print("Result:", arithmetic.subtract(num1, num2))
            elif choice == '3':
                print("Result:", arithmetic.multiply(num1, num2))
            elif choice == '4':
                print("Result:", arithmetic.divide(num1, num2))
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def geometry_menu():
    print("Geometry Menu:")
    print("1. Calculate Area")
    print("2. Calculate Perimeter")
    print("3. Back to main menu")

    while True:
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            shape = input("Enter the shape (square/rectangle/circle): ").lower()
            if shape == 'square':
                side = float(input("Enter the side length: "))
                print("Area:", geometry.calculate_area('square', side))
            elif shape == 'rectangle':
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                print("Area:", geometry.calculate_area('rectangle', length, width))
            elif shape == 'circle':
                radius = float(input("Enter the radius: "))
                print("Area:", geometry.calculate_area('circle', radius))
            else:
                print("Invalid shape.")
        elif choice == '2':
            shape = input("Enter the shape (square/rectangle/circle): ").lower()
            if shape == 'square':
                side = float(input("Enter the side length: "))
                print("Perimeter:", geometry.calculate_perimeter('square', side))
            elif shape == 'rectangle':
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                print("Perimeter:", geometry.calculate_perimeter('rectangle', length, width))
            elif shape == 'circle':
                radius = float(input("Enter the radius: "))
                print("Perimeter:", geometry.calculate_perimeter('circle', radius))
            else:
                print("Invalid shape.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def fractions_menu():
    print("Fractions Menu:")
    print("1. Add Fractions")
    print("2. Subtract Fractions")
    print("3. Multiply Fractions")
    print("4. Divide Fractions")
    print("5. Back to main menu")

    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = input("Enter the first fraction (e.g., 1/2): ")
            num2 = input("Enter the second fraction (e.g., 1/3): ")
            if choice == '1':
                print("Result:", fractions.add_fractions(num1, num2))
            elif choice == '2':
                print("Result:", fractions.subtract_fractions(num1, num2))
            elif choice == '3':
                print("Result:", fractions.multiply_fractions(num1, num2))
            elif choice == '4':
                print("Result:", fractions.divide_fractions(num1, num2))
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()