class InlineKeyboardButton:
    def __init__(self, text, url=None, callback_data=None):
        self.text = text
        self.url = url
        self.callback_data = callback_data

    def to_dict(self):
        d = {"text": self.text}
        if self.url:
            d["url"] = self.url
        if self.callback_data:
            d["callback_data"] = self.callback_data
        return d

class InlineKeyboardMarkup:
    def __init__(self, inline_keyboard):
        self.inline_keyboard = inline_keyboard  # List of lists of InlineKeyboardButton

    def to_dict(self):
        return {
            "inline_keyboard": [
                [button.to_dict() for button in row]
                for row in self.inline_keyboard
            ]
        }
