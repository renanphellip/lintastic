import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any, Dict

from lintastic.enums import LogMessage
from lintastic.utils.logger import Logger


class FunctionImporterService:
    def __init__(self, custom_functions_path: str, verbose=False):
        self.custom_functions_path = custom_functions_path
        self.verbose = verbose

    def __register_functions(self, module: ModuleType) -> Dict[str, Any]:
        imported_functions = {}
        for name, obj in vars(module).items():
            if not name.startswith('_'):
                if name in globals():
                    Logger.warning(
                        LogMessage.FUNCTION_ALREADY_EXISTS.format(
                            function_name=name
                        )
                    )
                else:
                    globals()[name] = obj
                    imported_functions[name] = obj
                    if self.verbose:
                        Logger.debug(
                            LogMessage.CUSTOM_FUNCTION_IMPORTED.format(
                                function_name=name
                            )
                        )
        return imported_functions

    def import_functions(self) -> Dict[str, Any]:
        custom_functions_path = (
            Path(self.custom_functions_path) / '__init__.py'
        )
        if not custom_functions_path.exists():
            Logger.error(
                LogMessage.INIT_NOT_FOUND.format(
                    custom_functions_path=self.custom_functions_path
                )
            )

        module_name = 'custom_functions'
        spec = importlib.util.spec_from_file_location(
            module_name, custom_functions_path
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        imported_functions = self.__register_functions(module)

        return imported_functions
