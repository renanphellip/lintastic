from typing import Any, Dict, Protocol


class IFileReader(Protocol):
    def read(self, file_path: str) -> Dict[str, Any]:
        ...
