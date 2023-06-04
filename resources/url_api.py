from flask_restful import Resource
from http import HTTPStatus
import time
from model.basic import UrlModel
from common.exceptions import BadRequest, InternalServerError
from services.url_shortner import UrlShortnerService


class UrlShortner(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        try:
            valid = UrlModel.load_data()
            short_url = UrlShortnerService().generate_short_url(valid.long_url)
            response = dict()
            response["long_url"] = valid.long_url
            response["short_url"] = short_url
            response["request_timestamp"] = int(time.time())
            return response, HTTPStatus.OK
        except BadRequest as e:
            return e.error_response, e.error_code
        except Exception as e:
            e = InternalServerError(str(e))
            return e.error_response, e.error_code
