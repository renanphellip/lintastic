from enum import Enum


class SupportedResultExtension(str, Enum):
    JSON = '.json'
    TXT = '.txt'
    MD = '.md'

    def __str__(self):
        return self.value
