import time
from logger import logger
from common.constants import Constant


def calculate_time(inner_function):
    def wrapper_function(*args, **kwargs):
        logger.info(f"started execution of {inner_function.__name__}")
        start_ts = time.time()
        rtn = inner_function(*args, **kwargs)
        end_ts = time.time()
        logger.info(f"{inner_function.__name__} execution took {end_ts-start_ts}s")
        return rtn

    return wrapper_function


def is_valid_url(url):
    """validates user provided url

    Args:
        url (str): given url

    Returns:
        bool: for valid url returns `True`
    """
    logger.info(f"validating regex for {url}")
    if Constant.URL_REGEX.match(url):
        return True, "url is valid"
    else:
        return False, "check scheme, domain, ip or port missing from url"


if __name__ == "__main__":
    print(is_valid_url("http://stackoverflow.com"))
    print(is_valid_url("https://www.google./"))
    print(is_valid_url("http://localhost:/url-shortner"))
