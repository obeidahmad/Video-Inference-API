import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from api.controller.inference_controller import router as inference_router
from domain.exceptions.input_exception import ApiException

app = FastAPI(title='Inference API')

app.include_router(inference_router,
                   prefix='/inference',
                   tags=['Prediction'])

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080)


@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exception: ApiException):
    return JSONResponse(status_code=400, content={"message": exception.message})


@app.exception_handler(Exception)
async def unexpected_exception_handler(request: Request, exception: Exception):
    return JSONResponse(status_code=500, content={"message": 'Unexpected server error.'})
