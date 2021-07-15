from flask import Flask, render_template, request
from hashids import Hashids

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LetsKeepItAsSecretBetweenYouAndMe'

hash_id = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        return render_template('index.html', short_url=url)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
