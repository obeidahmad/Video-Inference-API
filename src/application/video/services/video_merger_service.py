import os

import cv2

from domain.contracts.abstract_video_processing_service import AbstractVideoProcessingService
from shared.helpers.alphanumerical_sort_helper import sort_alphanumerical


class VideoMergerService(AbstractVideoProcessingService):
    def process_video(self, path) -> None:
        img_array = []

        frames = os.listdir(path)
        frames = sort_alphanumerical(frames)
        for filename in frames:
            print(filename)
            img = cv2.imread(os.path.join(path, filename))
            height, width = img.shape[:2]
            size = (width, height)
            img_array.append(img)

        out = cv2.VideoWriter('output/vid.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

        [out.write(image) for image in img_array]
        out.release()
