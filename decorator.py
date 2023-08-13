import functools
import time


def metric(fn):
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call')
        result = func(*args, **kwargs)
        print('end call')
        return result

    return wrapper


# 测试
@log
def my_function(x, y):
    return x + y


print(my_function(3, 5))


def log2(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(arg, str):
                print(f'{arg} begin call')
            else:
                print('begin call')
            result = func(*args, **kwargs)
            print('end call')
            return result

        return wrapper

    if callable(arg):
        return decorator(arg)
    else:
        return decorator


# 测试
@log2
def my_function1(x, y):
    return x + y


@log2('execute')
def my_function2(x, y):
    return x - y


print(my_function1(3, 5))
print(my_function2(10, 7))
