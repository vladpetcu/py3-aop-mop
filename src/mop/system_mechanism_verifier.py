from aspectlib import Aspect, Proceed, Return
from os import path
from .mop_log_error import MopLogError


class SystemMechanismVerifierMOP:
    ''' mechanism verification
    '''
    
    @Aspect
    def system_parameter_range_verification(class_instance, *args):
        (param1, param2) = args
        if not param1 > param2:
            raise MopLogError(class_instance, 'Error: invalid parameters')
        yield Proceed

    @Aspect
    def ensure_result_type(class_instance, *args):
        result = yield Proceed
        if not isinstance(result, str):
            raise MopLogError(class_instance, 'Error: Result must be a string')

