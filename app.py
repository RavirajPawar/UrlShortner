from flask import Flask, render_template, request, flash
import json
from helper_function import is_valid_url, generate_key

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LetsKeepItAsSecretBetweenYouAndMe'


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        if is_valid_url(url):
            response_from_cuttly = generate_key(url)
            with open("mapping.json", "r") as jsonFile:
                mapping_url = json.load(jsonFile)

            mapping_url[url] = response_from_cuttly['shortLink']

            with open("mapping.json", "w") as jsonFile:
                json.dump(mapping_url, jsonFile)
            return render_template('index.html', short_url=url)
        else:
            flash("Please Enter Valid Url")
            return render_template('index.html', short_url=url)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
