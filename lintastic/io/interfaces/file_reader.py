from abc import ABC, abstractmethod
from typing import Any, Dict


class IFileReader(ABC):
    @abstractmethod
    def read(file_path: str) -> Dict[str, Any]:
        pass
