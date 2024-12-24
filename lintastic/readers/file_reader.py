from typing import Any, Dict, Protocol


class IFileReader(Protocol):
    # ruff: noqa: PLR6301
    def read(self, file_path: str) -> Dict[str, Any]: ...
