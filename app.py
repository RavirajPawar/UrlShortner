from flask import Flask, render_template, request, flash
from helper_function import is_valid_url, generate_key, short_url_collection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LetsKeepItAsSecretBetweenYouAndMe'


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        if is_valid_url(url):
            response_from_cuttly = generate_key(url)
            mapping_url = short_url_collection()
            if url in mapping_url:
                return render_template('index.html', short_url=mapping_url[url])
            else:
                mapping_url[url] = response_from_cuttly['shortLink']
                short_url_collection(mapping_url, update=True)
                return render_template('index.html', short_url=response_from_cuttly['shortLink'])
        else:
            flash("Please Enter Valid Url")
            return render_template('index.html', short_url=url)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
