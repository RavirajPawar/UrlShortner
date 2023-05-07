import pyshorteners
from architecture.singleton import Singleton
from logger import logger
from common.utils import calculate_time


class UrlShortnerService(metaclass=Singleton):
    def __init__(self):
        self.conn = pyshorteners.Shortener()

    @calculate_time
    def generate_short_url(self, long_url):
        logger.info(f"got {long_url} for shorting")
        tmp = self.conn.tinyurl.short(long_url)
        logger.info(f"generated {tmp}")
        return tmp


if __name__ == "__main__":
    UrlShortnerService().generate_short_url("www.google.com")
