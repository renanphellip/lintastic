from dataclasses import dataclass
from typing import Any


@dataclass
class JSONPathMatch:
    context: str
    target_value: Any
