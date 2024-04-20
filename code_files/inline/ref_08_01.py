def convert_color(color):
    if isinstance(color, str) and color.startswith('#'):
        red = int(color[1:3], 16)
        green = int(color[3:5], 16)
        blue = int(color[5:7], 16)
        return red, green, blue
    else:
        return color

def main():
    # RGB to Hex conversion
    rgb_color = (255, 0, 0)
    hex_value = convert_color(rgb_color)
    print(f"RGB: {rgb_color} -> Hex: {hex_value}")

    # Hex to RGB conversion
    hex_color = '#00ff00'
    rgb_color = convert_color(hex_color)
    print(f"Hex: {hex_color} -> RGB: {rgb_color}")

if __name__ == "__main__":
    main()
