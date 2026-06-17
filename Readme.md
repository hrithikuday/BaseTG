# PyTgBot

Minimal Telegram Bot framework using `requests`.

## Features

- Simple and minimalistic API for building Telegram bots
- Middleware support for message preprocessing
- Custom message handlers with filters
- Easy message sending and editing (text, photo, audio, video)

## Installation

```sh
pip install .
```

## Usage

```python
from pytgbot import Bot, filters, middleware
from pytgbot.handler import on_message

# Example middleware
@middleware.use
def lowercase_text(message):
    if 'text' in message:
        message['text'] = message['text'].lower()
    return message

# Example handler for /start command
@on_message(filters.cmd("start"))
def start_handler(msg):
    msg.send("Welcome to the bot!")

# Example handler for a specific message
@on_message(filters.msg("hello"))
def hello_handler(msg):
    msg.send("Hi there!")

if __name__ == "__main__":
    bot = Bot("YOUR_BOT_TOKEN")
    bot.run()
```

## Project Structure

- [`pytgbot/bot.py`](pytgbot/bot.py): Main bot loop and update polling
- [`pytgbot/message.py`](pytgbot/message.py): Message object and send/edit methods
- [`pytgbot/filters.py`](pytgbot/filters.py): Message filter utilities
- [`pytgbot/handler.py`](pytgbot/handler.py): Handler registration
- [`pytgbot/middleware.py`](pytgbot/middleware.py): Middleware support

## License

MIT
