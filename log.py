
def timestamp(function1):
    import time
    def wrapper():
        print(time.ctime())
        return function1()
    return wrapper
    