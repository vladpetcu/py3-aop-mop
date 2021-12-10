from aspectlib import Aspect, Proceed, Return

class AOPBasic:

    @Aspect
    def with_basic_waver(*args):
        print(f'before calling {args} type: {type(args)}')
        yield Proceed
        print('after call')

    @Aspect(bind=True)
    def with_explicit_cutpoint_waver(cutpoint, *args):
        print(f'before calling {cutpoint} type: {type(cutpoint)}')
        yield Return('another_return_value')

    @Aspect
    def with_proceed_waver(*args):
        (cutpoint, initial_params) = args
        print(f'before calling, initial params: {initial_params}')
        yield Proceed(cutpoint, 'another_calling_params')
        print('after call')

    @Aspect
    def with_return_waver(*args):
        print('before calling')
        yield Return('another_return_value')

