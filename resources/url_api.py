from flask_restful import Resource
import time
from model.basic import UrlModel
from common.exceptions import BadRequest, InternalServerError
from services.url_shortner import UrlShortnerService
from logger import logger


class UrlShortner(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        logger.info("started processing /url-shortner".center(100, "*"))
        try:
            valid = UrlModel.load_data()
            short_url = UrlShortnerService().generate_short_url(valid.long_url)
            response = dict()
            response["long_url"] = valid.long_url
            response["short_url"] = short_url
            response["request_timestamp"] = int(time.time())
            logger.info("finished processing /url-shortner".center(100, "*"))
            return response
        except BadRequest as e:
            logger.warning(f"{e.__class__.__name__}: {str(e)}")
            return e.error_response, e.error_code
        except Exception as e:
            logger.error(f"{e.__class__.__name__}: {str(e)}", exc_info=True)
            e = InternalServerError(str(e))
            return e.error_response, e.error_code
