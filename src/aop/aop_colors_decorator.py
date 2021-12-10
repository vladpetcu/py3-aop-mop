from aspectlib import Aspect, Proceed, weave, weave_class
from colorama import Fore


class AopColorsDecorator:
    ''' AOP Colors Decorator - decorates classes print outputs with different colors
    '''

    _active = True
    _colors = [Fore.WHITE]

    def with_color(color=Fore.WHITE):

        def wrap(func):
            
            @Aspect(bind=True)
            def wrapped_func(cutpoint, *args):
                AopColorsDecorator._colors.append(color)
                print(color, end='')
                yield Proceed
                AopColorsDecorator._colors.pop()
                print(AopColorsDecorator._colors[-1], end='')
            
            return wrapped_func(func)
        
        return wrap


if AopColorsDecorator._active:
    from some_class import SomeClass
    
    # weave_class(SomeClass, AopColorsDecorator.with_color(color=Fore.GREEN))
    weave(SomeClass.method_with_green, AopColorsDecorator.with_color(color=Fore.GREEN))
