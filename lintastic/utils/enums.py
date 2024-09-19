from enum import Enum


class SupportedDocumentExtensions(Enum):
    YAML = '.yaml'
    YML = '.yml'
    JSON = '.json'


class SupportedOutputExtensions(Enum):
    JSON = '.json'
    TXT = '.txt'
