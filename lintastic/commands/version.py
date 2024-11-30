from lintastic.file_reader.file_reader_service import FileReaderService
from lintastic.logs import Logger, LogMessages


def version():
    file_reader_service = FileReaderService()
    data = file_reader_service.read_file('pyproject.toml')
    try:
        project_version = data['tool']['poetry']['version']
        if not project_version:
            raise KeyError
        Logger.info(
            LogMessages.DISPLAY_VERSION.format(
                lintastic_version=project_version
            )
        )
    except KeyError:
        Logger.error(LogMessages.VERSION_NOT_SPECIFIED)
