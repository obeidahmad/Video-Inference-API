import os

import cv2
import numpy as np
import requests

from domain.contracts.abstract_url_service import AbstractUrlService
from domain.contracts.abstract_openvino_service import AbstractOpenvinoService
from domain.contracts.abstract_path_service import AbstractPathService


class OpenvinoPredictionService(AbstractOpenvinoService):
    def __init__(self, path_service: AbstractPathService, api_url_service: AbstractUrlService):
        self.path_service: AbstractPathService = path_service
        self.api_url_service: AbstractUrlService = api_url_service

    def detect(self, input_image: str, model_name: str) -> None:
        try:
            url = self.api_url_service.urls.image_segmentation_url % model_name
            files = {'input_data': open(input_image, 'rb')}
            res = requests.post(url, files=files)
            jpg_as_np = np.frombuffer(res.content, dtype=np.uint8)
            img = cv2.imdecode(jpg_as_np, flags=1)
            frames_output_path = os.path.join(self.path_service.paths.frames_output_dir, os.path.basename(input_image))
            cv2.imwrite(frames_output_path, img)
        except Exception as e:
            print(e)
        os.remove(input_image)
