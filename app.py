# require Pillow lib

from PIL import Image

image = Image.open('./normal_image.jpg')

matrix = image.getdata()

width, height = image.size
average_image = Image.new('L', (width, height))

for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        average_pixel = (r + g + b) // 3
        average_image.putpixel((x, y), average_pixel)

average_image.save('gray_image-py.png')