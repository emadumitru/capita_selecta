# Peaceful Color Code Converter

def convert_rgb_to_hex(red, green, blue):
    """Converts RGB color code to hexadecimal color code"""
    hex_code = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return hex_code

def convert_hex_to_rgb(hex_code):
    """Converts hexadecimal color code to RGB color code"""
    red = int(hex_code[1:3], 16)
    green = int(hex_code[3:5], 16)
    blue = int(hex_code[5:7], 16)
    return red, green, blue

def main():
    # RGB to Hexadecimal Conversion
    red = 255
    green = 0
    blue = 0
    hex_code = convert_rgb_to_hex(red, green, blue)
    print(f"RGB: ({red}, {green}, {blue})")
    print(f"Hexadecimal: {hex_code}")

    # Hexadecimal to RGB Conversion
    hex_code = '#00ff00'
    red, green, blue = convert_hex_to_rgb(hex_code)
    print(f"Hexadecimal: {hex_code}")
    print(f"RGB: ({red}, {green}, {blue})")

if __name__ == "__main__":
    main()