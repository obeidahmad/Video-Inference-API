from fastapi import File, UploadFile, APIRouter

from containers import Container

router = APIRouter()
inference_service = Container.inference_service()


@router.post("/")
async def create_upload_file(model_name: str, uploaded_file: UploadFile = File(...)):
    return inference_service.run_inference(uploaded_file, model_name)

# http exception
