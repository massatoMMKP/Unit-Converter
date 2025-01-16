#temp converter

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def celsius_to_kelvin(celsius):
    return celsius + 273

def kelvin_to_celsius(kelvin):
    return kelvin - 273

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 1.8 + 273

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273) * 1.8 + 32

print("Welcome to the unit converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

while True:
    try:
        choice = input("Enter your choice (1-6): ")

        match choice:
            case "1":
                try:
                    celsius = float(input("Enter the temperature in Celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case "2":
                try:
                    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case "3":
                try:
                    celsius = float(input("Enter the temperature in Celsius: "))
                    kelvin = celsius_to_kelvin(celsius)
                    print(f"{celsius} Celsius is equal to {kelvin} Kelvin")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case "4":
                try:
                    kelvin = float(input("Enter the temperature in Kelvin: "))
                    celsius = kelvin_to_celsius(kelvin)
                    print(f"{kelvin} Kelvin is equal to {celsius} Celsius")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case "5":
                try:
                    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                    kelvin = fahrenheit_to_kelvin(fahrenheit)
                    print(f"{fahrenheit} Fahrenheit is equal to {kelvin} Kelvin")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case "6":
                try:
                    kelvin = float(input("Enter the temperature in Kelvin: "))
                    fahrenheit = kelvin_to_fahrenheit(kelvin)
                    print(f"{kelvin} Kelvin is equal to {fahrenheit} Fahrenheit")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
