import cv2
import numpy as np
import requests

from domain.contracts.abstract_openvino_service import AbstractOpenvinoService


class OpenvinoPredictionService(AbstractOpenvinoService):
    def detect(self, image: str, model_name: str) -> None:
        try:
            url = f'http://localhost:80/models/{model_name}/image_segmentation'
            print(image)
            files = {'input_data': open(image, 'rb')}
            res = requests.post(url, files=files)
            jpg_as_np = np.frombuffer(res.content, dtype=np.uint8)
            img = cv2.imdecode(jpg_as_np, flags=1)
            cv2.imwrite(f'output/frames/{image}', img)
        except Exception as e:
            print(e)

# path service and/or setting service (read from .json output dir and input dir) and inject service
# in the relevant service

# dependency injection (dependency injector)
