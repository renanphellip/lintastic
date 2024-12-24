from typing import List

from pydantic.dataclasses import dataclass

from lintastic.enums import Severity


@dataclass
class ValidationResult:
    rule: str
    context: str
    severity: Severity
    messages: List[str]
    documentations: List[str]


@dataclass
class ValidationSummary:
    total_errors: int
    total_warnings: int
    total_informations: int
    total_hints: int


@dataclass
class ValidationResultCollection:
    validation_results: List[ValidationResult]
    validation_summary: ValidationSummary
