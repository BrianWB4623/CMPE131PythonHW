def allcaps(function1):
    def wrapper():
        result=function1()
        return result.upper()
    return wrapper
