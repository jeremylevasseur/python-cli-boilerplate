from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls) -> list:
        return list(map(lambda c: c.value, cls))


class EnvironmentType(str, ExtendedEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class Locale(str, ExtendedEnum):
    EN_US = "en_US"


class LogLevel(str, ExtendedEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    TRACE = "TRACE"


class LogJustifyMethod(str, ExtendedEnum):
    DEFAULT = "default"
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    FULL = "full"
