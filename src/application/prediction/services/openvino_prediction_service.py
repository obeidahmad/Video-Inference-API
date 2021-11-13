import os

import cv2
import numpy as np
import requests

from domain.contracts.abstract_openvino_service import AbstractOpenvinoService
from domain.contracts.abstract_path_service import AbstractPathService


class OpenvinoPredictionService(AbstractOpenvinoService):
    def __init__(self, path_service: AbstractPathService):
        self.path_service: AbstractPathService = path_service

    def detect(self, image: str, model_name: str) -> None:
        try:
            url = f'http://localhost:80/models/{model_name}/image_segmentation'
            print(image)
            files = {'input_data': open(image, 'rb')}
            res = requests.post(url, files=files)
            jpg_as_np = np.frombuffer(res.content, dtype=np.uint8)
            img = cv2.imdecode(jpg_as_np, flags=1)
            frames_output_path = os.path.join(self.path_service.paths.frames_output_dir, os.path.basename(image))
            cv2.imwrite(frames_output_path, img)
        except Exception as e:
            print(e)
