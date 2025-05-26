from abc import ABC, abstractmethod
from typing import Any, Dict


class IFileReaderService(ABC):
    @abstractmethod
    def read_file(file_path: str) -> Dict[str, Any]:
        pass
