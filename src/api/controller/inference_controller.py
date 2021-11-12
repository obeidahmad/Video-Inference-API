from fastapi import File, UploadFile, APIRouter

from application.prediction.services.inference_service import InferenceService

router = APIRouter()
inference = InferenceService()


@router.post("/")
async def create_upload_file(model_name: str, uploaded_file: UploadFile = File(...)):
    return inference.run_inference(uploaded_file, model_name)

# http exception
