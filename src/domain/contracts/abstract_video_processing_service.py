from abc import ABCMeta, ABC, abstractmethod


class AbstractVideoProcessingService(ABC):
    metaclass = ABCMeta

    @abstractmethod
    def process_video(self, path) -> None:
        pass
