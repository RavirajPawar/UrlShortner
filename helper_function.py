from urllib.parse import urlparse
import requests


def is_valid_url(url):
    """
    This function checks passed url is valid or not
    url:- this is input url
    return:- True if passed url is valid else False
    """
    try:
        result = urlparse(url)
        # print("scheme", result.scheme, " netloc ", result.netloc)
        return all([result.scheme, result.netloc])

    except Exception as e:
        # print(e)
        return False


def generate_key(url):
    """
    url:- valid url
    return:- generated key
    """
    api_key = 'd6b2a44c4fa01e7795679c7b2deaaf6c3a31d'
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    data = requests.get(api_url).json()['url']
    print(data)
    if data['status'] == 7:
        return data
    else:
        return {"error": "something wrong happen"}


# generate_key("https://towardsdatascience.com/best-apis-for-url-shortening-using-python-2db09d1f86f0")
