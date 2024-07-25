import random
from PIL import Image

def swap_pixels(image, seed=None):
    # Encrypt the image by swapping pixels
    if seed is not None:
        random.seed(seed)  # Set the seed for reproducibility

    pixels = list(image.getdata())
    width, height = image.size

    for x in range(len(pixels)):
        i = random.randint(0, len(pixels) - 1)
        j = random.randint(0, len(pixels) - 1)
        pixels[i], pixels[j] = pixels[j], pixels[i]

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    return new_image

def swap_pixels_back(image, seed=None):
    # Decrypt the image by swapping pixels back
    if seed is not None:
        random.seed(seed)  # Set the seed for reproducibility

    pixels = list(image.getdata())
    width, height = image.size

    swaps = []
    for x in range(len(pixels)):
        i = random.randint(0, len(pixels) - 1)
        j = random.randint(0, len(pixels) - 1)
        swaps.append((i, j))

    # Reverse the swaps to get the original image back
    for i, j in reversed(swaps):
        pixels[i], pixels[j] = pixels[j], pixels[i]

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    return new_image

# Example usage
if __name__ == "__main__":
    # Load the image
    input_image = Image.open("image.png")

    # Encrypt the image
    encrypted_image = swap_pixels(input_image, seed=42)
    encrypted_image.save("encrypted_image.png")

    # Decrypt the image
    decrypted_image = swap_pixels_back(encrypted_image, seed=42)
    decrypted_image.save("decrypted_image.png")
