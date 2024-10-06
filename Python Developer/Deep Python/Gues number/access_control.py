from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def access_control(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') == ADMIN_USERNAME:
            result = func(*args, **kwargs)
            return result
        else:
            print(UNKNOWN_COMMAND)
    return wrapper
