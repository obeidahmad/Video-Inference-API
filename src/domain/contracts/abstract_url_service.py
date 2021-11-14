from abc import ABCMeta, ABC, abstractmethod

from domain.models.urls import Urls


class AbstractUrlService(ABC):
    metaclass = ABCMeta

    @abstractmethod
    def urls(self) -> Urls:
        pass
