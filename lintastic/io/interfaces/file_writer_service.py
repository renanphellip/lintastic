from abc import ABC, abstractmethod
from typing import Any


class IFileWriterService(ABC):
    @abstractmethod
    def write_file(output_path: str, data: Any) -> str:
        pass
