from urllib.parse import urlparse
from logger import logger


def is_valid_url(url):
    """validates user provided url

    Args:
        url (str): given url

    Returns:
        bool: for valid url returns `True`
    """
    try:
        result = urlparse(url)
        logger.info(f"scheme:\t{result.scheme} netloc:\t{result.netloc}")
        return all([result.scheme, result.netloc])

    except Exception as e:
        logger.warning(str(e), exc_info=True)
        return False
