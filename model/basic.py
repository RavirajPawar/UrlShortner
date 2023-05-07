from pydantic import BaseModel
from common.utils import is_valid_url
from logger import logger
from common.constants import Constant


class UrlModel(BaseModel):
    long_url: str

    class Config:
        extra = "forbid"

    @classmethod
    def load_data(cls, data):
        try:
            cls(**data)
            return is_valid_url(data["long_url"])
        except Exception as e:
            logger.warning(str(e), exc_info=True)
            if Constant.EXTRA_PARAMETER_ERROR in str(e):
                return False, Constant.EXTRA_PARAMETER_ERROR
            elif Constant.REQUIRED_PARAMETER_ERROR in str(e):
                return False, Constant.REQUIRED_PARAMETER_ERROR
            else:
                return False, Constant.GENERIC_ERROR


if __name__ == "__main__":
    print(UrlModel.load_data({"long_url": "https://stackoverflow.com"}))
    print(UrlModel.load_data({"long_url": "https://www.google.com/"}))
    print(UrlModel.load_data({"long_url": "http://localhost:5000/url-shortner"}))
