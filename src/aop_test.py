import aop
from some_class import SomeClass

if __name__ == '__main__':
    some_instance = SomeClass(3, 2)
    some_instance.method_one()
    print()

    some_instance.method_two()
    print()

    some_instance.method_three('calling_params')
    print()

    meth_four_result = some_instance.method_four()
    print(meth_four_result)
    print()

    some_instance.method_with_green()
    print()
    
    some_instance.method_with_debugger()
    print()

    some_instance.method_with_loop()
