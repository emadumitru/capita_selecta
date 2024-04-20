### Type: Color Code Convertor --- Style: Modular

# Color Code Converter

def rgb_to_hex(rgb):
    """Convert RGB color code to hexadecimal color code"""
    r, g, b = rgb
    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_code

def hex_to_rgb(hex_code):
    """Convert hexadecimal color code to RGB color code"""
    hex_code = hex_code.lstrip("#")
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    rgb = (r, g, b)
    return rgb

def main():
    # Convert RGB to Hex
    rgb_color = (255, 0, 0)
    hex_color = rgb_to_hex(rgb_color)
    print("RGB color:", rgb_color)
    print("Hex color:", hex_color)

    # Convert Hex to RGB
    hex_color = "#00ff00"
    rgb_color = hex_to_rgb(hex_color)
    print("Hex color:", hex_color)
    print("RGB color:", rgb_color)

if __name__ == "__main__":
    main()