import time
from my_queue.core.message import Message
from my_queue.core.singleton_queue import SingletonQueue

DISABLED = "disabled"
ENABLED = "enabled"


class Queue(metaclass=SingletonQueue):

    status = True

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.head = None
            self.initialized = True

    def append(self, message):
        if not self.status:
            return

        new_message = Message(message)
        new_message.set_timestamp(int(time.time()))

        if self.head is None:
            self.head = new_message
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_message

    def append_vip(self, message):
        if not self.status:
            return

        new_message = Message(message)
        new_message.next = self.head
        self.head = new_message

    def get_latest_message(self):
        if not self.status:
            return
        
        if self.head is None:
            return "The queue is Empty!"

        message = self.head
        if message.next is None:
            last_message = message.message
            self.head = None
            return last_message

        self.head = message.next

        return message.message

    """
    Get all messages in the queue and also return a tuple of messages an number of messages in the queue.
    Return: messages, total number of messages
    """
    def get_all_messages(self):
        if not self.status:
            return
        messages = []

        current = self.head
        while current:
            messages.append(current.message)
            current = current.next
        return messages, len(messages)

    def set_queue_status(self, desired_status):
        if desired_status == ENABLED:
            self.status = True

        if desired_status == DISABLED:
            self.status = False

        return self.status

    def get_queue_status(self):
        if self.status:
            status = ENABLED
        else:
            status = DISABLED

        return status
