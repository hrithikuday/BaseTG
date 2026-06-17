def cmd(command: str):
    def filter_func(message):
        return message.get('text', '').startswith(f"/{command}")
    return filter_func

def msg(text: str):
    def filter_func(message):
        return message.get('text', '') == text
    return filter_func

def group():
    def filter_func(message):
        chat_type = message.get('chat', {}).get('type', '')
        return chat_type in ('group', 'supergroup')
    return filter_func

def private():
    def filter_func(message):
        chat_type = message.get('chat', {}).get('type', '')
        return chat_type == 'private'
    return filter_func
