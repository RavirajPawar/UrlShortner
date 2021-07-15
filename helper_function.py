from urllib.parse import urlparse


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



