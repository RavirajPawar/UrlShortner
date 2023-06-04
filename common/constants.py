import re
from architecture.singleton import Singleton


class Constant(metaclass=Singleton):
    # NOTE: pydentic validation error changes with package version
    EXTRA_PARAMETER_ERROR = "(type=value_error.extra)"
    REQUIRED_PARAMETER_ERROR = "(type=value_error.missing)"
    URL_REGEX = re.compile(
        r"^(?:http|ftp)s?://"  # scheme
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or IP
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
