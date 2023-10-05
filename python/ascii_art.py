import sys
from PIL import Image

ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main():
    path = sys.argv[1]
    try:
        image = Image.open(path)
    except:
        print(f"Unable to open image file {path}.")
        return

    new_width = 100
    image = resize_image(image, new_width=new_width)
    image = grayify(image)

    pixels = pixels_to_ascii(image)
    len_pixels = len(pixels)

    ascii_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]
    ascii_image = "\n".join(ascii_image)

    print(ascii_image)

if __name__=='__main__':
    main()