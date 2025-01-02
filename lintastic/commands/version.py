from lintastic.enums.log_message import LogMessage
from lintastic.readers.file_reader_service import FileReaderService
from lintastic.utils.logger import Logger


def version():
    file_reader_service = FileReaderService()
    pyproject = file_reader_service.read_file('pyproject.toml')
    try:
        project_version = pyproject['tool']['poetry']['version']
        if not project_version:
            raise KeyError
        Logger.info(
            LogMessage.DISPLAY_VERSION.format(
                lintastic_version=project_version
            )
        )
    except KeyError:
        Logger.error(LogMessage.VERSION_NOT_SPECIFIED)
