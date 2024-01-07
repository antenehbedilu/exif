from fastapi import APIRouter, status
from models.health import Health

#create an instance of APIRouter
router = APIRouter(
    prefix='/api', #set the prefix for all routes under this router
    tags=['HealthChecks'] #assign tags to the router for documentation purposes
)

#endpoint for health check
@router.get('/health', response_model=Health, status_code=status.HTTP_200_OK)
def health_check():
    return Health
