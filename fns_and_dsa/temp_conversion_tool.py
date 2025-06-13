# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        temp = float(temp_input)  # Validate temperature input

        # Prompt user for the unit type
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Conversion logic
        if unit == "C":
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
