"""
Number Converter Program - Mission 5 (The Digital Detective)
Converts a user-supplied decimal (base-10) integer into binary (base-2) and hexadecimal (base-16).
"""

def main():
    print("==========================================")
    print("      Digital Detective Number Converter  ")
    print("==========================================")
    
    user_input = input("Enter a decimal number: ").strip()
    
    try:
        decimal_num = int(user_input)
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer.")
        return

    binary_val = bin(decimal_num)
    hex_val = hex(decimal_num)
    
    print("\n--- Conversion Results ---")
    print(f"Decimal (Base 10):     {decimal_num}")
    print(f"Binary (Base 2):       {binary_val}")
    print(f"Hexadecimal (Base 16): {hex_val.upper()}")
    print("--------------------------")

if __name__ == "__main__":
    main()
