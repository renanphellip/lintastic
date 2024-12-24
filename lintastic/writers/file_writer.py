from typing import Any, Protocol


class IFileWriter(Protocol):
    # ruff: noqa: PLR6301
    def write(output_path: str, data: Any) -> str: ...
