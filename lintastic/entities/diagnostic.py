from dataclasses import dataclass, field
from typing import List

from lintastic.enums import Severity


@dataclass
class Diagnostic:
    rule: str
    context: str
    severity: Severity
    messages: List[str]
    documentations: List[str]


@dataclass
class DiagnosticCollection:
    diagnostics: List[Diagnostic]
    total_errors: int = field(init=False)
    total_warnings: int = field(init=False)
    total_informations: int = field(init=False)
    total_hints: int = field(init=False)

    def __post_init__(self):
        self.total_errors = sum(
            1
            for diagnostic in self.diagnostics
            if diagnostic.severity == Severity.ERROR
        )
        self.total_warnings = sum(
            1
            for diagnostic in self.diagnostics
            if diagnostic.severity == Severity.WARN
        )
        self.total_informations = sum(
            1
            for diagnostic in self.diagnostics
            if diagnostic.severity == Severity.INFO
        )
        self.total_hints = sum(
            1
            for diagnostic in self.diagnostics
            if diagnostic.severity == Severity.HINT
        )
