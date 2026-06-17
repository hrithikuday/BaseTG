import requests

class Message:
    def __init__(self, data, base_url):
        self.data = data
        self.chat_id = data['chat']['id']
        self.text = data.get('text', '')
        self.message_id = data['message_id']
        self.base_url = base_url

    def send(self, text, reply_markup=None):
        data = {
            "chat_id": self.chat_id,
            "text": text
        }
        if reply_markup:
            # If reply_markup is an object with to_dict, convert it
            if hasattr(reply_markup, 'to_dict'):
                import json
                data["reply_markup"] = json.dumps(reply_markup.to_dict())
            else:
                import json
                data["reply_markup"] = json.dumps(reply_markup)
        response = requests.post(self.base_url + "sendMessage", data=data)
        if response.ok:
            result = response.json().get("result")
            if result:
                return Message(result, self.base_url)
        return None

    def send_photo(self, url, caption="", reply_markup=None):
        data = {
            "chat_id": self.chat_id,
            "photo": url,
            "caption": caption
        }
        if reply_markup:
            if hasattr(reply_markup, 'to_dict'):
                import json
                data["reply_markup"] = json.dumps(reply_markup.to_dict())
            else:
                import json
                data["reply_markup"] = json.dumps(reply_markup)
        response = requests.post(self.base_url + "sendPhoto", data=data)
        if response.ok:
            result = response.json().get("result")
            if result:
                return Message(result, self.base_url)
        return None

    def send_audio(self, url, caption=""):
        requests.post(self.base_url + "sendAudio", data={
            "chat_id": self.chat_id,
            "audio": url,
            "caption": caption
        })

    def send_video(self, url, caption=""):
        requests.post(self.base_url + "sendVideo", data={
            "chat_id": self.chat_id,
            "video": url,
            "caption": caption
        })

    def edit_msg(self, new_text):
        requests.post(self.base_url + "editMessageText", data={
            "chat_id": self.chat_id,
            "message_id": self.message_id,
            "text": new_text
        })

    def delete(self):
        """Delete this message via Telegram Bot API."""
        requests.post(self.base_url + "deleteMessage", data={
            "chat_id": self.chat_id,
            "message_id": self.message_id
        })

    def reply(self, text):
        requests.post(self.base_url + "sendMessage", data={
            "chat_id": self.chat_id,
            "text": text,
            "reply_to_message_id": self.message_id
        })
