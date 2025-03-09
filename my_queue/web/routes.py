from flask import Blueprint, jsonify, abort, request

from my_queue.controllers.queue_controller import QueueController
from my_queue.controllers.rabbit_controller import RabbitController


main = Blueprint('main', __name__)

queue_controller = QueueController()
rabbit_controller = RabbitController()


@main.route('/add', methods=['POST'])
def add():
    return queue_controller.add_list(request.json)


@main.route('/add_vip', methods=['POST'])
def add_vip():
    return queue_controller.add_vip(request.json)


@main.route('/delete', methods=['DELETE'])
def delete_player():
    return queue_controller.delete_player(request.json)


@main.route('/get_all_messages', methods=['GET'])
def get_all_messages():
    return queue_controller.get_all_messages()


@main.route('/queue_status', methods=['POST'])
def change_queue_status():
    return queue_controller.queue_status(request.json)


@main.route('/get_queue_status', methods=['GET'])
def get_queue_status():
    return queue_controller.get_queue_status()


@main.route('/get_latest_message', methods=['GET'])
def get_latest_message():
    return queue_controller.get_latest_message()


@main.route('/add_subs', methods=['POST'])
def add_subs():
    return rabbit_controller.add_to_queue(request.json)


@main.route('/bad_request')
def bad_request():
    abort(400)


@main.route('/server_error')
def server_error():
    abort(500)
