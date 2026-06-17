middlewares = []

def use(func):
    middlewares.append(func)
    return func

def apply_middlewares(message):
    for mw in middlewares:
        message = mw(message)
    return message
