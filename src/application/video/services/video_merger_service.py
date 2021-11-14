import os

import cv2

from domain.contracts.abstract_path_service import AbstractPathService
from domain.contracts.abstract_video_processing_service import AbstractVideoProcessingService
from shared.helpers.alphanumerical_sort_helper import sort_alphanumerical


class VideoMergerService(AbstractVideoProcessingService):
    def __init__(self, path_service: AbstractPathService):
        self.path_service: AbstractPathService = path_service

    def process_video(self, path) -> None:
        img_array = []
        frames = os.listdir(path)
        frames = sort_alphanumerical(frames)
        for frame in frames:
            if frame.endswith(".jpg"):
                image_path = os.path.join(path, frame)
                img = cv2.imread(image_path)
                height, width = img.shape[:2]
                size = (width, height)
                img_array.append(img)
                os.remove(image_path)

        video_output_path = os.path.join(self.path_service.paths.video_output_dir, "vid.avi")
        out = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

        [out.write(image) for image in img_array]
        out.release()
