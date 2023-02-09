from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.api import router as api_router

ROOT = Path(__file__).resolve().parent.parent

app = FastAPI(title="Menus API")

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    print(f'Menus API app from {ROOT} starts on port 8000')
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload=True)
