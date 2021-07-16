from urllib.parse import urlparse
import requests
import json

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
    # print(data)
    if data['status'] == 7:
        return data
    else:
        return {"error": "something wrong happen"}


def short_url_collection(mapping_url=None, update=False):
    """
    function reads centralized json file which keeps track of all original urls and shorter url for same
    update:- update file decides just read json or update json after reading json
    mapping_url:- dictionary with added new entry
    returns:- all key value pair of original url as key and short url as value
    """
    if update:
        with open("mapping.json", "w") as jsonFile:
            json.dump(mapping_url, jsonFile)
    else:
        with open("mapping.json", "r") as jsonFile:
            return json.load(jsonFile)


# generate_key("https://towardsdatascience.com/best-apis-for-url-shortening-using-python-2db09d1f86f0")
