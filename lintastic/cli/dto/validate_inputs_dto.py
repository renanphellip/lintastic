from dataclasses import dataclass
from typing import Optional


@dataclass
class ValidateInputsDTO:
    document_path: str
    ruleset_path: str
    results_path: Optional[str]
    output_format: str
    verbose: bool
