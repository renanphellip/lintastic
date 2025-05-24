from abc import ABC, abstractmethod
from typing import Any, Dict


class IFileReaderService(ABC):
    @abstractmethod
    def read_file(self, file_path: str) -> Dict[str, Any]:
        pass
