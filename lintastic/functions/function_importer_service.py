import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any, Dict

from lintastic.enums.log_message import LogMessage
from lintastic.utils.logger import Logger


class FunctionImporterService:
    def __init__(self, functions_path: str, verbose=False, globals: Dict[str, Any]=globals()):
        self.functions_path = functions_path
        self.verbose = verbose
        self.globals = globals

    def __register_functions(self, module: ModuleType) -> Dict[str, Any]:
        imported_functions = {}
        for name, obj in vars(module).items():
            if not name.startswith('_'):
                if name in self.globals:
                    Logger.warning(
                        LogMessage.FUNCTION_ALREADY_EXISTS.format(
                            function_name=name
                        )
                    )
                else:
                    imported_functions[name] = obj
                    if self.verbose:
                        Logger.debug(
                            LogMessage.FUNCTION_IMPORTED.format(
                                function_name=name
                            )
                        )
        return imported_functions

    def import_functions(self) -> Dict[str, Any]:
        functions_path = (
            Path(self.functions_path) / '__init__.py'
        )
        if not functions_path.exists():
            Logger.error(
                LogMessage.INIT_NOT_FOUND.format(
                    functions_path=self.functions_path
                )
            )

        module_name = 'functions'
        spec = importlib.util.spec_from_file_location(
            module_name, functions_path
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        imported_functions = self.__register_functions(module)

        return imported_functions
