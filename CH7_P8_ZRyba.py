"""
File: testgrayscale.py
Tests a function for converting a color image to
grayscale.
"""

from images import Image

def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
            sepia(image)
def sepia(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif red < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)            
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            image.setPixel(x, y, (r, g, b))
def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    grayscale(image)
    print("Close the image window to quit. ")
    image.draw()

if __name__ == "__main__":
   main()
