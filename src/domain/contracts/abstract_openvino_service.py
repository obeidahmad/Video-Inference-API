from abc import ABCMeta, ABC, abstractmethod


class AbstractOpenvinoService(ABC):
    metaclass = ABCMeta

    @abstractmethod
    def detect(self, image: str, model_name: str) -> None:
        pass
