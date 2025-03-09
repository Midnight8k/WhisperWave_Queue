from my_queue.core.rabbit import Rabbit
from flask import jsonify
import json


class RabbitController:
    queue = None

    def __init__(self):
        self.message = Rabbit()

    def add_to_queue(self, message_data):
        p1 = json.dumps(message_data)
        message_data_parsed = json.loads(p1)

        tts = message_data_parsed["message"]

        self.message.set_connection()
        self.message.set_queue_name("tts")
        self.message.send_message(tts)
        self.message.close_connection()       

        return jsonify({"Messages": "The message {} added to the queue".format(tts)})
