from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError
from flask import request
from common.utils import is_valid_url
from logger import logger
from common.exceptions import BadRequest
from common.constants import Constant


class UrlModel(BaseModel):
    long_url: str

    class Config:
        extra = "forbid"

    @classmethod
    def load_data(cls):
        logger.info("started validation for request")
        try:
            data = request.get_json()
            valid = cls(**data)
            is_valid_url(data["long_url"])
            logger.info(f"finished validation for request {data}")
            return valid
        except ValidationError as e:
            logger.warning(f"ValidationError :{str(e)}")
            message = (
                str(e)
                .replace("UrlModel", "request parameters ")
                .replace(Constant.EXTRA_PARAMETER_ERROR, "")
                .replace(Constant.REQUIRED_PARAMETER_ERROR, "")
                .strip()
            )
            raise BadRequest(message=message)
        except Exception as e:
            logger.error(f"Failed request validation :{str(e)}", exc_info=True)
            message = str(e)
            raise BadRequest(message=message)


if __name__ == "__main__":
    print(UrlModel.load_data({"long_url": "https://stackoverflow.com"}))
    print(UrlModel.load_data({"long_url": "https://www.google.com/"}))
    print(UrlModel.load_data({"long_url": "http://localhost:5000/url-shortner"}))
