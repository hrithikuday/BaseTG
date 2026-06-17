import requests, time
from .middleware import apply_middlewares
from .handler import handlers
from .message import Message

class Bot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.offset = None

    def run(self):
        print("🤖 Bot is running...")
        while True:
            try:
                res = requests.get(self.base_url + "getUpdates", params={
                    "offset": self.offset,
                    "timeout": 30
                })
                updates = res.json()["result"]
                for update in updates:
                    if "message" in update:
                        message_data = apply_middlewares(update["message"])
                        msg = Message(message_data, self.base_url)
                        for filt, func in handlers:
                            if filt(message_data):
                                func(msg)
                                break
                        self.offset = update["update_id"] + 1
                    elif "callback_query" in update:
                        cq = update["callback_query"]
                        # Synthesize a message-like dict for compatibility
                        cq_data = {
                            'chat': cq['message']['chat'],
                            'message_id': cq['message']['message_id'],
                            'data': cq.get('data', ''),
                            'from': cq['from'],
                        }
                        msg = Message(cq_data, self.base_url)
                        for filt, func in handlers:
                            if filt(cq_data):
                                func(msg)
                                break
                        self.offset = update["update_id"] + 1
                time.sleep(1)
            except Exception as e:
                print("Error:", e)
                time.sleep(2)
