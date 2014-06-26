def my_decorator(func):
    def callable():
        print 'Decorating....'
        r = func()
        print r
        print 'Done decorating....'
        return r
    return callable


@my_decorator
def decorated_function():
    print 'Executing decorated function'
    return 'Return Value'


result = decorated_function()
print 'Result = ' + result