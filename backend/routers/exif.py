from fastapi import APIRouter

#create an instance of APIRouter
router = APIRouter(
    prefix='/api', #set the prefix for all routes under this router
    tags=['Exif']) #assign tags to the router for documentation purposes

#directory path to store images
IMG_DIR = 'img/'
#list of MIME types supported by Exif
mime_type = ['image/jpeg', 'image/png', 'image/tiff', 'image/webp']
#maximum file size in bytes that can be uploaded
FILE_SIZE = 26214400 #25MB (1MB = 1,048,576 Bytes)
