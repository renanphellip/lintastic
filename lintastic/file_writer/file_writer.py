from typing import Any, Protocol


class IFileWriter(Protocol):
    def write(output_path: str, data: Any) -> str: ...
