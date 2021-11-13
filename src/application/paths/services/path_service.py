import json

from domain.contracts.abstract_path_service import AbstractPathService
from domain.models.paths import Paths


class PathService(AbstractPathService):
    def __init__(self):
        with open('assets/paths.json') as paths:
            self.paths: Paths = Paths.parse_obj(json.load(paths))

    def paths(self) -> Paths:
        return self.paths
