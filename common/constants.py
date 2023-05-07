import re
from architecture.singleton import Singleton


class Constant(metaclass=Singleton):
    SUCEESS = 200
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
    EXTRA_PARAMETER_ERROR = "extra fields not permitted"
    REQUIRED_PARAMETER_ERROR = "field required"
    GENERIC_ERROR = "something went wrong"
    URL_REGEX = re.compile(
        r"^(?:http|ftp)s?://"  # scheme
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or IP
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
