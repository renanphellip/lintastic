from enum import Enum


class JSONSchemaDraft(str, Enum):
    AUTO = 'auto'
    DRAFT4 = 'draft4'
    DRAFT6 = 'draft6'
    DRAFT7 = 'draft7'
    DRAFT201909 = 'draft2019-09'
    DRAFT202012 = 'draft2020-12'

    def __str__(self):
        return self.value
