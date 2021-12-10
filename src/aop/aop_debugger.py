from inspect import currentframe, getsource, getfullargspec, getfile, findsource
from aspectlib import Aspect, Return, weave
from colorama import Fore, Style
from datetime import datetime
from pynput import keyboard
from textwrap import dedent


debugger_break_point = None

class AopDebugger:
    ''' AOP Debugger
    '''
    
    _diagnose = False
    __registered_func_call = {}
    
    def __register(called_function, function_caller, function_args, function_path, line_numb, datetime):
        AopDebugger.__registered_func_call = {
            'function': called_function,
            'caller': function_caller,
            'arguments': function_args,
            'path': (function_path, line_numb),
            'datetime': datetime,
        }

    def __on_debug_step_over(key):
        if key.char == 'c':
            return False
    
    def break_point():
        frame = currentframe()
        try:
            exec_locals = frame.f_back.f_locals
            exec_line_number = frame.f_back.f_lineno
        finally:
            del frame
        
        registered_func = AopDebugger.__registered_func_call
        func_def_line_numb = registered_func['path'][1]

        print('\n' + Fore.YELLOW + f"Breakpoint [{registered_func['datetime']}]")
        print(f"<Definition path>\n\t{registered_func['path'][0]}], line {func_def_line_numb}")
        print(f"<Function/method>\n\t{registered_func['function']},"
            f" breakpoint at line {exec_line_number - 1 + func_def_line_numb}")
        print(f"<Caller>\n\t{registered_func['caller']}")
        print(f'<Arguments>')
        for arg in registered_func['arguments']:
            print(f'\t{arg}')
        print('<Local variables>')
        for key in exec_locals.keys():
            print(f'\t{key}: {exec_locals[key]}')
        print(Style.RESET_ALL)

        with keyboard.Listener(on_release=AopDebugger.__on_debug_step_over) as listener:
            listener.join()


    def with_debugger(*params):
        
        def wrap(func):

            def build_function_source(func, caller = None):
                func_source = getsource(func)
                new_source = dedent(func_source)

                if caller:
                    arg_names = getfullargspec(func).args
                    if len(arg_names):
                        caller_class_name = type(caller).__name__
                        self_pointer = arg_names[0]
                        new_source = new_source.replace(f'{self_pointer}.__', f'{self_pointer}._{caller_class_name}__')

                new_source = new_source.replace('aop.debugger_break_point', 'AopDebugger.break_point()')
                return new_source

            @Aspect(bind=True)
            def wrapped_func(cutpoint, *args, **kwargs):
                (caller_object, *rest_args) = args
                func_definition_path = getfile(func)
                func_definition_line_numb = findsource(func)[1] + 1

                AopDebugger.__register(
                    cutpoint,
                    caller_object,
                    args,
                    func_definition_path,
                    func_definition_line_numb,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                )

                built_func_source = build_function_source(cutpoint, caller_object)
                exec(built_func_source, globals()) # do not modify locals
                newly_function = globals()[f'{func.__name__}']

                result = newly_function(*args, **kwargs)
                yield Return(result)
            
            return wrapped_func(func)
    
        return wrap

if AopDebugger._diagnose:
    from some_class import SomeClass

    weave(SomeClass.method_with_debugger, AopDebugger.with_debugger())
