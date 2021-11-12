import glob

from fastapi import UploadFile
from starlette.responses import FileResponse

from application.prediction.services.openvino_prediction_service import OpenvinoPredictionService
from application.video.services.video_merger_service import VideoMergerService
from application.video.services.video_splitter_service import VideoSplitterService
from shared.helpers.alphanumerical_sort_helper import sort_alphanumerical


class InferenceService:
    def __init__(self):
        self.splitter = VideoSplitterService()
        self.uploader = OpenvinoPredictionService()
        self.merger = VideoMergerService()

    def run_inference(self, uploaded_file: UploadFile, model_name: str) -> FileResponse:
        file_location = f"input/{uploaded_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(uploaded_file.file.read())

        self.splitter.process_video(file_location)

        frames = glob.glob('./*.jpg')
        frames = sort_alphanumerical(frames)
        [self.uploader.detect(filename, model_name) for filename in frames]

        self.merger.process_video("output/frames/")

        response = FileResponse("output/vid.avi", media_type="video/x-msvideo")
        response.headers["Content-Disposition"] = "attachment; filename=vid.avi"
        return response
