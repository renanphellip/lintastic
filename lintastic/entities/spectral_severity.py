from enum import Enum


class SpectralSeverity(str, Enum):
    ERROR = 'error'
    WARN = 'warn'
    INFO = 'information'
    HINT = 'hint'

    def __str__(self):
        return self.value
