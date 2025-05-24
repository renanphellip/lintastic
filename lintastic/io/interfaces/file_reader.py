from abc import ABC, abstractmethod
from typing import Any, Dict


class IFileReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> Dict[str, Any]:
        pass
