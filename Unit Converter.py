def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Centimeter to Meter")
    print("4. Meter to Centimeter")

    choice = int(input("Enter option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} km = {value * 1000} m")
    elif choice == 2:
        print(f"{value} m = {value / 1000} km")
    elif choice == 3:
        print(f"{value} cm = {value / 100} m")
    elif choice == 4:
        print(f"{value} m = {value * 100} cm")
    else:
        print("Invalid choice")


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")

    choice = int(input("Enter option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} kg = {value * 1000} g")
    elif choice == 2:
        print(f"{value} g = {value / 1000} kg")
    elif choice == 3:
        print(f"{value} kg = {value * 2.20462} lb")
    elif choice == 4:
        print(f"{value} lb = {value / 2.20462} kg")
    else:
        print("Invalid choice")


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Enter option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == 2:
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == 3:
        print(f"{value}°C = {value + 273.15} K")
    elif choice == 4:
        print(f"{value} K = {value - 273.15}°C")
    else:
        print("Invalid choice")


# ---------- MAIN PROGRAM ----------
while True:
    print("\n========== UNIT CONVERTER ==========")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Exit")

    main_choice = int(input("Enter your choice: "))

    if main_choice == 1:
        length_converter()
    elif main_choice == 2:
        weight_converter()
    elif main_choice == 3:
        temperature_converter()
    elif main_choice == 4:
        print("Thank you for using Unit Converter!")
        break
    else:
        print("Invalid choice. Please try again.")
