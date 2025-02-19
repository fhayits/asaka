version = "0.0.1"


def wrapp(original_func):
    def wrapper(wrapp_func):
        wrapp_func.__name__ = original_func.__name__
        wrapp_func.__doc__ = original_func.__doc__
        wrapp_func.__qualname__ = original_func.__qualname__
        wrapp_func.__dict__ | original_func.__dict__
        return wrapp_func

    return wrapper


class Main:
    pass


class Point:
    pass
