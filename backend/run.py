import uvicorn

#run a FastAPI application using uvicorn with specific configuration options
if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8080,
        log_level='info',
        reload=True)
