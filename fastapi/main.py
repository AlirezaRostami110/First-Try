import uvicorn



if __name__ == '__main__':
    uvicorn.run('config:app', port=8002, reload=True)