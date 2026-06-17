def callback_data(data: str):
    def filter_func(message):
        # For callback_query updates, data is in the root dict, not in 'text'
        return message.get('data') == data
    return filter_func
