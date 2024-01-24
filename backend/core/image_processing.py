from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from uuid import uuid4

def generate_filename(file):
    #extract the file extension
    extension = file.filename.split('.')[-1]
    #generate a unique filename using UUID and the original file extension
    file.filename = f'{str(uuid4())}.{extension}'

def open_image(img: str):
    #opens an image using the provided file path 
    image = Image.open(img)
    return image

def read_exif(image):
    #check if 'exif' exists in the 'info' attribute of the image
    if 'exif' in image.info:
        #create an empty dictionary to store the extracted exif data
        exif = {}
        #iterate over each key-value pair in the exif data
        for key, value in image._getexif().items():
            #check if the key is present in the TAGS dictionary
            if key in TAGS:
                #map the key to its corresponding tag name and store the value in the exif dictionary
                exif[TAGS[key]] = value
        #check if the key exists from exif dictionary and return value else None
        date_time = exif.get('DateTimeOriginal')
        width = exif.get('ExifImageWidth')
        height = exif.get('ExifImageHeight')
        manufacturer = exif.get('Make')
        model = exif.get('Model')
        lens = exif.get('LensModel')
        aperture = exif.get('FNumber')
        focal_length = exif.get('FocalLength')
        exposure_time = exif.get('ExposureTime')
        iso = exif.get('ISOSpeedRatings')
        flash = exif.get('Flash')
        #extract specific exif data and store it in a separate dictionary
        exif_data = {
                'date_time': datetime.strptime(date_time, '%Y:%m:%d %H:%M:%S'),
                'width': width,
                'height': height,
                'manufacturer': manufacturer,
                'model': model,
                'lens': lens,
                'aperture': round(aperture, 1),
                'focal_length': round(focal_length, 1),
                'exposure_time': exposure_time,
                'iso': iso,
                'flash': flash}
        return exif_data
