from flask_restful import Resource
import time
from flask import request, make_response
from model.basic import UrlModel
from common.constants import Constant
from services.url_shortner import UrlShortnerService


class UrlShortner(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        data = request.get_json()
        status, msg = UrlModel.load_data(data)
        if not status:
            error_response = {
                "error_msg": "failed url validation.",
                "explanation": msg,
                "request_data": data,
                "request_timestamp": int(time.time()),
            }
            response = make_response(error_response)
            response.status_code = Constant.BAD_REQUEST
            return response
        short_url = UrlShortnerService().generate_short_url(data["long_url"])
        data["short_url"] = short_url
        data["request_timestamp"] = int(time.time())
        return data
