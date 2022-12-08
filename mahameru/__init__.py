import os
from flask import Flask
from bson.json_util import dumps
from .model import db
from . import user


def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config.from_pyfile('settings.cfg', silent=True)
    app.register_blueprint(user.bp)

    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    @app.route('/')
    def index():
        print("test")
        return "Mahameru Chat"
    
    @app.route('/chats')
    def join_table():
        joined = db.get_chat_collection()
        hasil = dumps(joined)
        app.logger.debug(hasil)
        return hasil
    
    return app
