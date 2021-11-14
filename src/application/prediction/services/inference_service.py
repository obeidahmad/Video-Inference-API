import glob
import os

from fastapi import UploadFile
from starlette.responses import FileResponse

from domain.contracts.abstract_openvino_service import AbstractOpenvinoService
from domain.contracts.abstract_path_service import AbstractPathService
from domain.contracts.abstract_video_processing_service import AbstractVideoProcessingService
from shared.helpers.alphanumerical_sort_helper import sort_alphanumerical


class InferenceService:
    def __init__(self, splitter_service: AbstractVideoProcessingService, uploader_service: AbstractOpenvinoService,
                 merger_service: AbstractVideoProcessingService, path_service: AbstractPathService):
        self.splitter: AbstractVideoProcessingService = splitter_service
        self.uploader: AbstractOpenvinoService = uploader_service
        self.merger: AbstractVideoProcessingService = merger_service
        self.path_service: AbstractPathService = path_service

    def run_inference(self, uploaded_file: UploadFile, model_name: str) -> FileResponse:
        file_input_location = os.path.join(self.path_service.paths.video_input_dir, uploaded_file.filename)
        with open(file_input_location, "wb+") as file_object:
            file_object.write(uploaded_file.file.read())

        self.splitter.process_video(file_input_location)

        frames = glob.glob(self.path_service.paths.frames_input_dir + "/*.jpg")
        frames = sort_alphanumerical(frames)
        [self.uploader.detect(frame, model_name) for frame in frames]

        self.merger.process_video(self.path_service.paths.frames_output_dir)

        output_video = os.path.join(self.path_service.paths.video_output_dir, "vid.avi")
        response = FileResponse(output_video, media_type="video/x-msvideo")
        response.headers["Content-Disposition"] = "attachment; filename=vid.avi"
        return response
