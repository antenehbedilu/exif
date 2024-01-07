from pydantic import BaseModel

#create a Health model
class Health(BaseModel):
    status: str = 'OK'
