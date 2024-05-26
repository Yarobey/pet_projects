from PIL import Image
from colorama import init

init()

CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def load_image(path):
    # Risize so that image would fit the terminal
    img = Image.open(path).resize((631, 533))
    width, height = img.size[0], img.size[1]
    pixels = img.load()
    pixel_list = []
    for j in range(height):
        pixel_list.append([pixels[i,j] for i in range(width)])
    img.close()
    return pixel_list

def brightness_matrix(pixels, mode=lambda R,G,B: (R+G+B)/3):
    height, width = len(pixels), len(pixels[0])
    matrix = []
    for i in range(height):
        new_row = []
        for j in range(width):
            R, G, B = pixels[i][j][0], pixels[i][j][1], pixels[i][j][2]
            new_row.append(round(mode(R,G,B)))
        matrix.append(new_row)
    return matrix

def to_ascii(matrix):
    border = round(256 / len(CHARS))
    height, width = len(matrix), len(matrix[0])
    image = []
    for i in range(height):
        new_row = []
        for j in range(width):
            group = matrix[i][j] // border
            new_row.append(CHARS[group]*3)
        image.append(new_row)
    return image

def draw(matrix):
    for i in range(len(matrix)):
        # Add "'\033[32m' + " to print to change the colour of the output
        print(''.join(matrix[i]))

def invert_brightness(matrix):
    height, width = len(matrix), len(matrix[0])
    for i in range(height):
        for j in range(width):
            matrix[i][j] = abs(matrix[i][j] - 255)


# Modes for the brightness_matrix
min_max = lambda R,G,B: (max(R, G, B) + min(R, G, B)) / 2
luminosity = lambda R,G,B: 0.21*R + 0.72*G + 0.07*B

pixels = load_image("ascii-pineapple.jpg")
matrix = brightness_matrix(pixels, luminosity)
# invert_brightness(matrix)
image = to_ascii(matrix)

draw(image)
