from flask import Flask
from flask_restful import Api

from resources.url import UrlShortner

app = Flask(__name__)
app.config["SECRET_KEY"] = "LetsKeepItAsSecretBetweenYouAndMe"

api = Api(app)
api.add_resource(UrlShortner, "/url-shortner")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
