from flask import Flask, render_template, request, flash
from hashids import Hashids
from helper_function import is_valid_url
app = Flask(__name__)
app.config['SECRET_KEY'] = 'LetsKeepItAsSecretBetweenYouAndMe'

hash_id = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        if is_valid_url(url):
            return render_template('index.html', short_url=url)
        else:
            flash("Please Enter Valid Url")
            return render_template('index.html', short_url=url)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
