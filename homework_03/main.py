import uvicorn
from fastapi import FastAPI

from src.routes import api_router

app = FastAPI(title="Menus API")

app.include_router(api_router)

if __name__ == '__main__':
    print(f'Menus API starts on port 8000')
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload=True)
