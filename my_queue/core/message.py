class Message:

    timestamp = None
    message = None
    def __init__(self, message=None):
        self.set_message(message)
        self.next = None

    def get_message(self):
        return self.message
    
    def set_message(self, message):
        self.message = message

    def get_timestamp(self):
        return self.timestamp
    
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
