import aop # due to eval, this has to be imported like this
from mop.system_mechanism_verifier import SystemMechanismVerifierMOP
from mop.resource_usage import ResourceUsageMOP


class SomeClass:

    @SystemMechanismVerifierMOP.system_parameter_range_verification
    def __init__(self, param1: int, param2: int) -> None:
        pass

    @aop.AOPBasic.with_basic_waver
    def method_one(self):
        print('SomeClass: method_one')

    @aop.AOPBasic.with_explicit_cutpoint_waver
    def method_two(self):
        print('SomeClass: method_two')
    
    @aop.AOPBasic.with_proceed_waver
    def method_three(self, param):
        print(f'SomeClass: method_three {param}')
    
    @aop.AOPBasic.with_return_waver
    @SystemMechanismVerifierMOP.ensure_result_type
    def method_four(self):
        print('SomeClass: method_four')
        return 'return_value'

    def method_with_green(self):
        print('I am green')

    def method_with_debugger(self):
        local_var = 1
        aop.debugger_break_point
        local_var = 2
        aop.debugger_break_point
        print('SomeClass: method_with_debugger done')

    @ResourceUsageMOP.with_cpu_usage
    def method_with_loop(self):
        a = 1
        for i in range(100):
            a += a * i
