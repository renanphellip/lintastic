from abc import ABC, abstractmethod
from typing import Any


class IFileWriter(ABC):
    @abstractmethod
    def write(output_path: str, data: Any) -> str:
        pass
