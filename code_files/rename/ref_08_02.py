import random

def generate_random_color_code():
    color_code = ""
    for _ in range(6):
        color_code += random.choice("0123456789ABCDEF")
    return color_code

def convert_to_rgb(color_code):
    red = int(color_code[0:2], 16)
    green = int(color_code[2:4], 16)
    blue = int(color_code[4:6], 16)
    return red, green, blue

def convert_to_hex(rgb):
    red = hex(rgb[0])[2:].zfill(2)
    green = hex(rgb[1])[2:].zfill(2)
    blue = hex(rgb[2])[2:].zfill(2)
    return red + green + blue

def main():
    color_code = generate_random_color_code()
    print("Generated Color Code:", color_code)
    
    rgb = convert_to_rgb(color_code)
    print("RGB:", rgb)
    
    converted_color_code = convert_to_hex(rgb)
    print("Converted Color Code:", converted_color_code)

if __name__ == "__main__":
    main()
