from http import HTTPStatus
import time


class BadRequest(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.error_msg = message
        self.error_code = HTTPStatus.BAD_REQUEST
        self.request_timestamp = int(time.time())
        self.error_response = {
            "error_msg": self.error_msg,
            "request_timestamp": self.request_timestamp,
            "error_code": self.error_code,
        }


class InternalServerError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.error_msg = message
        self.error_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.request_timestamp = int(time.time())
        self.error_response = {
            "error_msg": self.error_msg,
            "request_timestamp": self.request_timestamp,
            "error_code": self.error_code,
        }
