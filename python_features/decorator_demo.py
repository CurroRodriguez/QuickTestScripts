import timeit
import time

def my_decorator(func):
    def callable():
        print 'Decorating....'
        r = func()
        print r
        print 'Done decorating....'
        return r
    return callable






class MyDecoratorClass(object):

    def __init__(self, id=None):
        self.id = id or '9999'

    def __call__(self, func):
        self.func = func
        return self.caller

    def caller(self, *args, **kwargs):
        print self.id
        r = self.func(*args, **kwargs)
        print r
        return r



class TimedDecorator(object):

    def __init__(self, id):
        self.id = id


    def __call__(self, decorated):
        self.decorated = decorated
        return self.timed_invocation


    def timed_invocation(self, *args, **kwargs):
        start = timeit.default_timer()
        result = self.decorated(*args, **kwargs)
        end = timeit.default_timer()
        print self.decorated.__name__ + ' took ' + str(end - start) + ' milliseconds'
        return result


timed = TimedDecorator


@MyDecoratorClass()
def decorated_function():
    print 'Executing decorated function'
    return 'Return Value'


@MyDecoratorClass('1')
def another_decorated_function(a, b):
    return a + b




@timed('long_process')
def long_process():
    time.sleep(2)
    print 'Executed....'


@timed('long_calculation')
def long_calculation(n):
    time.sleep(n)
    return n



long_process()
r = long_calculation(3)
print r  