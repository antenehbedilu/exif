from fastapi import APIRouter, status, HTTPException, UploadFile
from models.exif import Exif
from uuid import uuid4
from core.image_processing import open_image, read_exif
from core.validator import validate_file

#create an instance of APIRouter
router = APIRouter(
    prefix='/api', #set the prefix for all routes under this router
    tags=['Exif']) #assign tags to the router for documentation purposes

#directory path to store images
IMG_DIR = 'img/'

@router.post('/view', response_model=Exif, status_code=status.HTTP_200_OK)
async def view_exif(file: UploadFile):
    #ensure file's content type and size meet the specified requirements
    await validate_file(file)
    #extract the file extension
    extension = file.filename.split('.')[-1]
    #generate a unique filename using UUID and the original file extension
    file.filename = f'{str(uuid4())}.{extension}'
    #put the file pointer at the start of the file, so that the next read will read the same content again
    await file.seek(0)
    #read the image data
    image = await file.read()
    #save the image to the specified directory
    with open(f'{IMG_DIR}{file.filename}', 'wb') as f:
        f.write(image)
    #open the saved image
    image = open_image(f'{IMG_DIR}{file.filename}')
    #read the Exif data from the image
    exif_data = read_exif(image)
    #if there is Exif data available for the image, return it
    if exif_data:
        return exif_data
    #when the image doesn't contain any Exif data, raise an HTTP exception
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
