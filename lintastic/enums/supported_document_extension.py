from enum import Enum


class SupportedDocumentExtension(str, Enum):
    YAML = '.yaml'
    YML = '.yml'
    JSON = '.json'

    def __str__(self):
        return self.value
