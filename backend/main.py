from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import health, exif
from core.validator import validate_dir

@asynccontextmanager
async def lifespan(app: FastAPI):
    #on startup
    #check if directory exists else create one
    validate_dir()
    yield
    #on shutdown

#create an instance of FastAPI and customize metadata configurations
app = FastAPI(
        docs_url='/api/docs', #set the URL for the API documentation
        openapi_url='/api/openapi', #set the URL for the OpenAPI schema
        redoc_url='/api/redoc', #disable the ReDoc documentation
        title='Exif', #set the title of the API
        description='This **RESTful API** is designed to modify **Exif** *(exchangeable image file format)* metadata.', #set the description of the API
        summary='Exif easily view, edit, and remove metadata.', #set a summary for the API
        version='0.0.1', #set the version of the API
        contact={ #set the contact information for the API
            'name': 'Exif',
            'url': 'https://github.com/antenehbedilu/exif',
            'email': 'hello@antenehbedilu.com'
            },
        license_info={ #set the license information for the API
            'name': 'MIT License',
            'url': 'https://raw.githubusercontent.com/antenehbedilu/exif/main/LICENSE'
            },
        lifespan=lifespan #run events on starts up and shutting down
        )

#include the health router in the FastAPI application
app.include_router(health.router)
#include the exif router in the FastAPI application
app.include_router(exif.router)
