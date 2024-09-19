from enum import Enum


class OutputFormat(str, Enum):
    TXT = 'text'
    JSON = 'json'
    NONE = 'none'

    def __str__(self):
        return self.value
