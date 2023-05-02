import pytesseract

from PIL import Image
# # Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    # Open the image using Pillow library
    with Image.open(image_path) as img:
        # Pass the image to PyTesseract to extract the text
        text = pytesseract.image_to_string(img)
        print(text)
        # Split the text into lines
        lines = text.split('\n')
        # Initialize an empty list to store the key-value pairs
        output = []
        # Loop through each line and split it into key-value pairs using the second space separator
        for line in lines:
            if ' ' in line:
                key, value = line.rsplit(' ', 1)
                # Strip leading and trailing whitespaces from the key and value
                key = key.strip()
                value = value.strip()
                # Add the key-value pair to the list
                output.append({key: value})
        return output

result = extract_text('Picture1.png')
# Iterate over the list of dictionaries and print each key-value pair on a separate line
for d in result:
    for key, value in d.items():
        print(key, ":", value)
