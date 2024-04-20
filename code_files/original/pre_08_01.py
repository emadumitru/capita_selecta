### Type: Color Code Convertor --- Style: Rigorous

def rgb_to_hex(red, green, blue):
    hex_value = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return hex_value

def hex_to_rgb(hex_value):
    red = int(hex_value[1:3], 16)
    green = int(hex_value[3:5], 16)
    blue = int(hex_value[5:7], 16)
    return red, green, blue

def main():
    # RGB to Hex conversion
    red = 255
    green = 0
    blue = 0
    hex_value = rgb_to_hex(red, green, blue)
    print(f"RGB: ({red}, {green}, {blue}) -> Hex: {hex_value}")

    # Hex to RGB conversion
    hex_value = '#00ff00'
    red, green, blue = hex_to_rgb(hex_value)
    print(f"Hex: {hex_value} -> RGB: ({red}, {green}, {blue})")

if __name__ == "__main__":
    main()