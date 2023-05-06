from pydantic import BaseModel
from common.utils import is_valid_url


class Url(BaseModel):
    long_url: str

    class Config:
        extra = "forbid"

    @classmethod
    def valid_url(cls, data):
        try:
            cls(*data)
        except Exception as e:
            pass
