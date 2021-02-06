from PIL import Image, ImageDraw
import numpy as np


def open_image(path):
    newImage = Image.open(path)
    return newImage


# Save Image
def save_image(image, path):
    image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image


# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


def Coloring():
    img = Image.open("C:/Users/18563/Documents/Nguyen Lab Documents/Aneurysm/descending_thoracic_aorta_sample.PNG")
    width, height = img.size
    # print(width,height)
    pixels = img.load()
    descending_label = (255, 0, 0)
    ascending_label = (0, 255, 0)
    descending = []
    descending_height = []
    descending_width = []
    ascending = []
    ascending_height = []
    ascending_width = []
    for i in range(width):
        for j in range(height):
            if pixels[i, j] == descending_label:
                descending.append((i, j))
            if pixels[i, j] == ascending_label:
                ascending.append((i, j))
            else:
                pixels[i, j] = (0, 0, 0)
    for pixel in descending:
        pixels[pixel[0], pixel[1]] = (255, 255, 255)
        descending_width.append(pixel[0])
        descending_height.append(pixel[1])
    for pixel in ascending:
        # print(pixel[0], pixel[1])
        pixels[pixel[0], pixel[1]] = (127, 127, 127)
        ascending_width.append(pixel[0])
        ascending_height.append(pixel[1])
    mean_location_descending = ((np.amax(descending_width) + np.min(descending_width)) / 2, (np.amax(descending_height) + np.min(descending_height)) / 2)
    mean_location_descending = round(mean_location_descending[0]), round(mean_location_descending[1])
    print(mean_location_descending)
    ImageDraw.floodfill(img, mean_location_descending, value=(255, 255, 255))
    mean_location_ascending = ((np.amax(ascending_width) + np.min(ascending_width)) / 2, (np.amax(ascending_height) + np.min(ascending_height)) / 2)
    mean_location_ascending = round(mean_location_ascending[0]), round(mean_location_ascending[1])
    print(mean_location_ascending)
    ImageDraw.floodfill(img, mean_location_ascending, value=(127, 127, 127))
    imagepath = ("C:/Users/18563/Documents/Nguyen Lab Documents/Aneurysm/descending_thoracic_aorta_sample2.PNG")
    img.save(imagepath)


Coloring()
