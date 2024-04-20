# Color Code Converter

def convert_color(color_code):
    """Convert color code between RGB and hexadecimal formats"""
    if isinstance(color_code, str) and color_code.startswith("#"):
        # Convert Hex to RGB
        color_code = color_code.lstrip("#")
        r = int(color_code[0:2], 16)
        g = int(color_code[2:4], 16)
        b = int(color_code[4:6], 16)
        rgb = (r, g, b)
        return rgb
    else:
        # Convert RGB to Hex
        r, g, b = color_code
        hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return hex_code

def main():
    # Convert RGB to Hex
    rgb_color = (255, 0, 0)
    hex_color = convert_color(rgb_color)
    print("RGB color:", rgb_color)
    print("Hex color:", hex_color)

    # Convert Hex to RGB
    hex_color = "#00ff00"
    rgb_color = convert_color(hex_color)
    print("Hex color:", hex_color)
    print("RGB color:", rgb_color)

if __name__ == "__main__":
    main()