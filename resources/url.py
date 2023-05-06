from flask_restful import Resource


class UrlShortner(Resource):
    def get(self):
        return {"hello": "world"}
