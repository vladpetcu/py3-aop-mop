from datetime import datetime
from .safe_file_writer import SafeFileWriter


class FileWriter:
    ''' MOP File Writer
    '''

    @SafeFileWriter.ensure_file_path_valid
    def __init__(self, file_path: str = ''):
        self.file_path = file_path
        self.__fd = None

    @property
    def fd(self):
        return self.__fd

    @SafeFileWriter.ensure_open_succeeded
    def open_file(self, mode='a'):
        self.__fd = open(self.file_path, mode)

    @SafeFileWriter.ensure_file_is_open
    def write(self, message):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__fd.write(f'[{now}] ')
        self.__fd.write(message + '\n')

    @SafeFileWriter.ensure_file_is_open
    def close(self):
        self.__fd.close()
        self.__fd = None
