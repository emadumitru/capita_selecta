def convert_color(color_code):
    def hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb_code):
        return '#%02x%02x%02x' % rgb_code

    if color_code.startswith('#'):
        rgb = hex_to_rgb(color_code)
        print(f"Hex code {color_code} converted to RGB: {rgb}")
    else:
        rgb = tuple(map(int, color_code.split(',')))
        hex_code = rgb_to_hex(rgb)
        print(f"RGB code {color_code} converted to Hex: {hex_code}")

# Convert hex code to RGB
hex_color = "#FF0000"
convert_color(hex_color)

# Convert RGB code to hex
rgb_color = "255,0,0"
convert_color(rgb_color)