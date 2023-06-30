# Temperature / measurement converter

# Steps:
# Ask the user what unit they want to convert and give multiple choices that can be used as input to choose
def main():
    print("\nTemperature / Measurement Converter App")
    print("""
    What units would you like to convert?
    Fahrenheit to Celsius (a)
    Celcius to Fahrenheit (b)
    Inches to Centimeters (c)
    Centimeters to Inches (d)
    """)


# Convert
def farh_to_cel():
    fahrenheit = input("Please type the temperature in fahrenheit: ")
    conversion = (int(fahrenheit) - 32) * 5/9
    print(f"The temperature in celcius is {round(conversion, 2)}° C.")
    main()


def cel_to_farh():
    celcius = input("Please type the temperature in celcius: ")
    conversion = (int(celcius) * 9/5) + 32
    print(f"The temperature in fahrenheit is {round(conversion, 2)}° F.")
    main()


def inch_to_cen():
    inches = input("Please type the measurement in inches: ")
    conversion = int(inches) * 2.54
    print(f"The measurement in centimeters is {round(conversion, 2)}cm.")
    main()


def cen_to_inch():
    cen = input("Please type the measurement in centimeters: ")
    conversion = int(cen) / 2.54
    print(f"The measurement in inches is {round(conversion, 2)}in.")
    main()

    
main()
choice = input("Please type the letter corresponding to your choice: ").lower()

if choice == "a":
    farh_to_cel()
elif choice == "b":
    cel_to_farh()
elif choice == "c":
    inch_to_cen()
elif choice == "d":
    cen_to_inch()
else:
    print("You did not input a valid choice. Please type again.")
    main()
    choice