from PIL import Image
from PIL.ExifTags import TAGS

def open_image(img: str):
    #opens an image using the provided file path 
    image = Image.open(img)
    return image
