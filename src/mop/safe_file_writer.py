from os import path
from aspectlib import Proceed, Aspect
from .mop_log_error import MopLogError


class SafeFileWriter:

    @Aspect
    def ensure_file_path_valid(class_instance, *args):
        (file_path) = args[0]
        if not path.exists(path.dirname(file_path)):
            raise MopLogError(class_instance, 'Error: The specified file path directory does not exist')
        yield Proceed

    @Aspect
    def ensure_open_succeeded(class_instance, *args):
        if class_instance.fd is not None:
            raise MopLogError(class_instance, 'Error: The file is already opened')
        yield Proceed
        if class_instance.fd is None:
            raise MopLogError(class_instance, 'Error: File could not be opened')

    @Aspect
    def ensure_file_is_open(class_instance, *args):
        if class_instance.fd is None:
            raise MopLogError(class_instance, 'Error: Open must be called before write/close')
        yield Proceed
        