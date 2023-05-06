import logging
from architecture.singleton import Singleton


class CustomLogger(metaclass=Singleton):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] - [%(levelname)s] - [%(filename)s:%(lineno)d] - %(message)s "
        )

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)


logger = CustomLogger().logger
