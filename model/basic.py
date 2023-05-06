from pydantic import BaseModel
from common.utils import is_valid_url
from logger import logger


class Url(BaseModel):
    long_url: str

    class Config:
        extra = "forbid"

    @classmethod
    def valid_url(cls, data):
        try:
            cls(**data)
            return is_valid_url(data["long_url"])
        except Exception as e:
            logger.warning(str(e), exc_info=True)
            return False


if __name__ == "__main__":
    print(Url.valid_url({"long_url": "https://stackoverflow.com"}))
    print(Url.valid_url({"long_url": "https://www.google.com/"}))
    print(Url.valid_url({"long_url": "http://localhost:5000/url-shortner"}))
