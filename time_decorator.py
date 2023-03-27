def timer(func):
    """
    Декоратор, що виводить час, який зайняв
    виконання декорованої функції.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.process_time()
        res = func(*args, **kwargs)
        print(func.__name__, time.process_time() - t)
        return res
    return wrapper

@timer
def sum(a,b):
    for i in range(1,10000000):
        a = a+b
    print(a)

sum(7,1)
