import cv2

from domain.contracts.abstract_video_processing_service import AbstractVideoProcessingService


class VideoSplitterService(AbstractVideoProcessingService):
    def process_video(self, path) -> None:
        vidcap = cv2.VideoCapture(path)
        success, image = vidcap.read()
        count = 0
        while success:
            cv2.imwrite("%d.jpg" % count, image)
            success, image = vidcap.read()
            count += 1
