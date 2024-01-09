from pydantic import BaseModel
from datetime import datetime

#create a Exif model to list all Exif data
class Exif(BaseModel):
    #made all the request body optional because clients don't necessarily send request bodies all the time
    date_time: datetime | None = None #DateTimeOriginal
    width: int | None = None #ExifImageWidth 
    height: int | None = None #ExifImageHeight 
    manufacturer: str | None = None #Make
    model: str | None = None #Model
    lens: str | None = None #LensModel
    aperture: float | None = None #FNumber
    focal_length: float | None = None #FocalLength
    exposure_time: float | None = None #ExposureTime
    iso: int | None = None #ISOSpeedRatings
    flash: int | None = None #Flash
