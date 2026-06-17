handlers = []

def on_message(filter_func):
    def wrapper(func):
        handlers.append((filter_func, func))
        return func
    return wrapper
