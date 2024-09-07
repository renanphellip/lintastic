from typing import Any, Dict, Protocol


class FileReader(Protocol):
    def read(self, file_path: str) -> Dict[str, Any]:
        ...
