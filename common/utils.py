from logger import logger
from common.constants import Constant


def is_valid_url(url):
    """validates user provided url

    Args:
        url (str): given url

    Returns:
        bool: for valid url returns `True`
    """
    logger.info(f"validating regex for {url}")
    logger.info(Constant.URL_REGEX.match(url))
    if Constant.URL_REGEX.match(url):
        return True, "url is valid"
    else:
        return False, "check scheme, domain, ip or port missing from url"


if __name__ == "__main__":
    print(is_valid_url("http://stackoverflow.com"))
    print(is_valid_url("https://www.google./"))
    print(is_valid_url("http://localhost:/url-shortner"))
