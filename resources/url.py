from flask_restful import Resource
from flask import request, make_response
from model.basic import Url


class UrlShortner(Resource):
    def get(self):
        return {"hello": "world"}
    
    def post(self):
        data = request.get_json()
        if not Url.valid_url(data): # TODO: valid url functionality 
            response = make_response({"error_msg": "failed url validation"})
            response.status_code = 400 # Invalid request
            return response
        return data
