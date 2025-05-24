import ast
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List

from lintastic.core.enums.log_message import LogMessage
from lintastic.utils.logger import Logger


class FunctionImporterService:
    def __init__(
        self,
        globals: Dict[str, Any] = globals(),
    ):
        self.globals = globals

    def import_functions(self, functions_path: str) -> Dict[str, Any]:
        functions_init_path = self._get_functions_init_path(functions_path)
        self._validate_functions_init_path(functions_init_path)

        declared_functions = self._extract_functions_from_init(functions_init_path)
        module = self._load_module(functions_init_path, declared_functions)

        imported_functions = self._register_functions(module)

        return imported_functions

    @staticmethod
    def _get_functions_init_path(functions_path: str) -> Path:
        return Path(functions_path) / '__init__.py'

    @staticmethod
    def _validate_functions_init_path(functions_init_path: Path) -> None:
        if not functions_init_path.exists():
            functions_path = functions_init_path.parent
            Logger.error(LogMessage.INIT_NOT_FOUND.format(functions_path=functions_path))

    @staticmethod
    def _extract_functions_from_init(functions_init_path: Path) -> List[str]:
        try:
            with open(functions_init_path, 'r', encoding='utf-8') as file:
                tree = ast.parse(file.read(), filename=str(functions_init_path))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == '__all__' for target in node.targets) and isinstance(node.value, ast.List):
                        return [elt.s for elt in node.value.elts if isinstance(elt, ast.Constant)]
        except Exception as error:
            Logger.error(LogMessage.FAIL_TO_PARSE_DUNDER_ALL_FROM_INIT.format(functions_init_path=functions_init_path, error=error))
        return []

    @staticmethod
    def _load_module(functions_init_path: Path, declared_functions: List[str]) -> ModuleType:
        try:
            module_name = 'functions'
            spec = importlib.util.spec_from_file_location(module_name, functions_init_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            return module
        except Exception as error:
            missing_functions = set(declared_functions) - set(dir(module))
            if missing_functions:
                Logger.error(
                    LogMessage.FAIL_TO_IMPORT_WITH_MISSING_FUNCTIONS.format(
                        functions_init_path=functions_init_path,
                        missing_functions=missing_functions,
                        error=error,
                    )
                )
            else:
                Logger.error(LogMessage.FAIL_TO_IMPORT_FUNCTIONS.format(functions_init_path=functions_init_path, error=error))

    def _register_functions(self, module: ModuleType) -> Dict[str, Any]:
        imported_functions = {}
        for name, obj in vars(module).items():
            if not name.startswith('_'):
                if name in self.globals:
                    Logger.warning(LogMessage.FUNCTION_ALREADY_EXISTS.format(function_name=name))
                else:
                    imported_functions[name] = obj
                    Logger.debug(LogMessage.FUNCTION_IMPORTED.format(function_name=name))
        return imported_functions
