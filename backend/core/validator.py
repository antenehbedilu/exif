from fastapi import HTTPException, status
from pathlib import Path

#list of MIME types supported by Exif
mime_type = ['image/jpeg', 'image/png', 'image/tiff', 'image/webp']
#maximum file size in bytes that can be uploaded
FILE_SIZE = 26214400 #25MB (1MB = 1,048,576 Bytes)

def validate_dir():
    #create a directory if it doesn't exists
    Path('./img/').mkdir(parents=True, exist_ok=True)

async def validate_file(file):
    #ensure file's MIME types matches our mime_type
    if file.content_type not in mime_type:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    #ensure file size remains below 25MB
    if len(await file.read()) >= FILE_SIZE:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
