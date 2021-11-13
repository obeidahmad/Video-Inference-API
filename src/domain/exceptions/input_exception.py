class ApiException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NotVideoFileException(ApiException):
    pass
