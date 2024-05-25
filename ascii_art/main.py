from PIL import Image


CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def load_image(path):
    img = Image.open(path)
    width, height = img.size[0], img.size[1]
    pixels = img.load()
    pixel_list = []
    for j in range(height):
        pixel_list.append([pixels[i,j] for i in range(width)])
    img.close()
    return pixel_list

def brightness_matrix(pixels):
    height, width = len(pixels), len(pixels[0])
    matrix = []
    for i in range(height):
        new_row = []
        for j in range(width):
            r, g, b = pixels[i][j][0], pixels[i][j][1], pixels[i][j][2]
            new_row.append((r+g+b)//3)
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
        print(''.join(matrix[i]))


pixels = load_image("ascii-pineapple.jpg")
# print(pixels)

matrix = brightness_matrix(pixels)
# print(matrix)

image = to_ascii(matrix)
# print(image)

draw(image)
# print("Successfully loaded image!")
# print(f"Image size: {(img.size)[0]} x {(img.size)[1]}")
