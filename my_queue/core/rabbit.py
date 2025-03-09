import time

import pika
from pika import exceptions


class Rabbit:
    connection = None
    channel = None
    queue = None

    url = "rabbitmq"

    def __init__(self):
        pass

    def set_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.url, heartbeat=60))

    def __set_channel(self):
        self.channel = self.connection.channel()

    def set_queue_name(self, queue_name):
        self.queue = queue_name

    def send_message(self, message):
        self.__set_channel()
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

        for _ in range(10):
            self.connection.process_data_events()

    def close_connection(self):
        self.connection.close()
