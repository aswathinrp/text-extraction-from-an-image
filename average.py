from PIL import Image

def get_average_color(image):
    
    # Resize the image to a small size to reduce processing time
    size = 100, 100
    image.thumbnail(size)

    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Calculate the average color of the image using the getpixel() method
    width, height = image.size
    r_total, g_total, b_total = 0, 0, 0
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r_total += r
            g_total += g
            b_total += b

    # Calculate the average RGB values
    pixel_count = width * height
    r_avg = r_total // pixel_count
    g_avg = g_total // pixel_count
    b_avg = b_total // pixel_count

    return r_avg, g_avg, b_avg
# Open the image file
image = Image.open('Picture1.png')

# Get the average color of the image
average_color = get_average_color(image)

# Print the average color in RGB format
print('Average color:', average_color)
