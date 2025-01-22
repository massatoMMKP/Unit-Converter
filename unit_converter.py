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
                while True:
                    try:
                        celsius = float(input("Enter the temperature in Celsius: "))
                        fahrenheit = celsius_to_fahrenheit(celsius)
                        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            case "2":
                while True:
                    try:
                        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                        celsius = fahrenheit_to_celsius(fahrenheit)
                        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            case "3":
                while True:
                    try:
                        celsius = float(input("Enter the temperature in Celsius: "))
                        kelvin = celsius_to_kelvin(celsius)
                        print(f"{celsius} Celsius is equal to {kelvin} Kelvin")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            case "4":
                while True:
                    try:
                        kelvin = float(input("Enter the temperature in Kelvin: "))
                        celsius = kelvin_to_celsius(kelvin)
                        print(f"{kelvin} Kelvin is equal to {celsius} Celsius")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            case "5":
                while True:
                    try:
                        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                        kelvin = fahrenheit_to_kelvin(fahrenheit)
                        print(f"{fahrenheit} Fahrenheit is equal to {kelvin} Kelvin")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            case "6":
                while True:
                    try:
                        kelvin = float(input("Enter the temperature in Kelvin: "))
                        fahrenheit = kelvin_to_fahrenheit(kelvin)
                        print(f"{kelvin} Kelvin is equal to {fahrenheit} Fahrenheit")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
