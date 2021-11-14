import json

from domain.contracts.abstract_url_service import AbstractUrlService
from domain.models.urls import Urls


class ApiUrlService(AbstractUrlService):
    def __init__(self):
        with open('assets/api_urls.json') as urls:
            self.urls: Urls = Urls.parse_obj(json.load(urls))

    def urls(self) -> Urls:
        return self.urls
