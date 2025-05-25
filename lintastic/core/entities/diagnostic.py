from dataclasses import dataclass, field
from typing import List

from lintastic.core.enums.severity import Severity


@dataclass
class Diagnostic:
    rule: str
    context: str
    severity: Severity
    messages: List[str]
    documentations: List[str]


@dataclass
class DiagnosticSummary:
    total_errors: str
    total_warnings: str
    total_informations: str
    total_hints: str


@dataclass
class DiagnosticCollection:
    diagnostics: List[Diagnostic]
    summary: DiagnosticSummary = field(init=False)

    def __post_init__(self):
        total_errors = str(sum(1 for diagnostic in self.diagnostics if diagnostic.severity == Severity.ERROR))
        total_warnings = str(sum(1 for diagnostic in self.diagnostics if diagnostic.severity == Severity.WARN))
        total_informations = str(sum(1 for diagnostic in self.diagnostics if diagnostic.severity == Severity.INFO))
        total_hints = str(sum(1 for diagnostic in self.diagnostics if diagnostic.severity == Severity.HINT))
        self.summary = DiagnosticSummary(total_errors, total_warnings, total_informations, total_hints)
