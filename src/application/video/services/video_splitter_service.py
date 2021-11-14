import os

import cv2

from domain.contracts.abstract_path_service import AbstractPathService
from domain.contracts.abstract_video_processing_service import AbstractVideoProcessingService
from domain.exceptions.input_exception import NotVideoFileException


class VideoSplitterService(AbstractVideoProcessingService):
    def __init__(self, path_service: AbstractPathService):
        self.path_service: AbstractPathService = path_service

    def process_video(self, path) -> None:
        video_capture = cv2.VideoCapture(path)
        success, image = video_capture.read()
        if not success:
            raise NotVideoFileException(message='File is not a Video.')
        count = 0
        while success:
            frames_input_path = os.path.join(self.path_service.paths.frames_input_dir, f"{count}.jpg")
            cv2.imwrite(frames_input_path, image)
            success, image = video_capture.read()
            count += 1
