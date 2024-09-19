from enum import Enum


class SupportedOutputExtensions(str, Enum):
    JSON = '.json'
    TXT = '.txt'

    def __str__(self):
        return self.value
