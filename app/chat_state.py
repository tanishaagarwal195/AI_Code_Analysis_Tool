# keeping this so that the AI session editable/extendable.

class ChatState:
    def __init__(self):
        self.messages = []

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})

    def add_ai_message(self, content):
        self.messages.append({"role": "assistant", "content": content})

    def get_conversation(self):
        return self.messages
