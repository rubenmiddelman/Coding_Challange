"""
 # @ Author: Ruben Middelman
 # @ Create Time: 2023-10-30 15:13:19
 # @ Modified by: Ruben Middelman
 # @ Modified time: 2023-10-30 15:18:29
 # @ Description:
Small program to convert image to ascii image is crooked, i dont know why
 """

from PIL import Image


f = open("img.txt", "a")


def image_to_ascii(image_path, width):
    img = Image.open(image_path)
    img = img.convert("L")  # Convert image to grayscale

    # Calculate new height while maintaining aspect ratio
    aspect_ratio = img.width / img.height
    new_height = int(width / aspect_ratio)

    img = img.resize((width, new_height))  # Resize image
    pixels = img.getdata()

    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    ascii_image = ""
    for pixel_value in pixels:
        ascii_image += ascii_chars[
            pixel_value // 25
        ]  # Map intensity to ASCII character

        if len(ascii_image) % width - 35 == 0:
            ascii_image += "\n"  # Add newline after each row
    f.write(ascii_image)


# Replace 'your_image.jpg' with the path to your image file
image_to_ascii("tux.png", 100)
