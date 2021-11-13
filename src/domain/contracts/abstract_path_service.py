from abc import ABCMeta, ABC, abstractmethod

from domain.models.paths import Paths


class AbstractPathService(ABC):
    metaclass = ABCMeta

    @abstractmethod
    def paths(self) -> Paths:
        pass
