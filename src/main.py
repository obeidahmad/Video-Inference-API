import uvicorn
from fastapi import FastAPI

from api.controller.inference_controller import router as inference_router

app = FastAPI(title='Inference API')

app.include_router(inference_router,
                   prefix='/inference',
                   tags=['Prediction'])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080)
