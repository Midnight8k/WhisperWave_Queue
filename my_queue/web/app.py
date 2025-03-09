from flask import Flask
from my_queue.web.routes import main as main_blueprint
from my_queue.web.erros import register_error_handler


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)
    register_error_handler(app)

    return app


def run():
    my_queue_app = create_app()
    my_queue_app.run(debug=False, host='0.0.0.0', port=2000)
