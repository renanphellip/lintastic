from dataclasses import dataclass


@dataclass
class ResolveInputsDTO:
    document_path: str
    output_path: str
    verbose: bool
