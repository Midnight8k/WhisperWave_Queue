import json
from flask import jsonify
from my_queue.core.queue import Queue


class QueueController:
    queue = None

    def __init__(self):
        self.queue = Queue()

    def add_list(self, message_data):
        p1 = json.dumps(message_data)
        message_data_parsed = json.loads(p1)

        message = message_data_parsed["message"]

        self.queue.append(message)
        return jsonify({"Messages": "The message {} added to the queue".format(message)})

    def add_vip(self, message_data):
        p1 = json.dumps(message_data)
        message_data_parsed = json.loads(p1)

        message = message_data_parsed["message"]

        self.queue.append_vip(message)
        return jsonify({"Messages": "The vip message {} added to the queue".format(message)})

    def delete_message(self, message_data):
        p1 = json.dumps(message_data)
        message_data_parsed = json.loads(p1)

        message = message_data_parsed["message"]
        self.queue.delete_message(message)
        return jsonify({"Messages": "The message {} deleted from the queue".format(message)})

    def get_latest_message(self):
        return jsonify({"Message": self.queue.get_latest_message()})

    def get_all_messages(self):
        messages, numb_messages = self.queue.get_all_messages()
        return jsonify({"Messages": messages, "TotalMessages": numb_messages})

    def queue_status(self, message_data):
        p1 = json.dumps(message_data)
        message_data_parsed = json.loads(p1)

        status = message_data_parsed["status"]
        self.queue.set_queue_status(status.lower())
        return jsonify({"Status": "The status of the queue is: {}".format(status)})

    def get_queue_status(self):
        return jsonify({"Status": self.queue.get_queue_status()})
