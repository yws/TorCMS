# -*- coding:utf-8 -*-
__author__ = 'bk'

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()



def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)

    # 附加路由和自定义的错误页面

    from .controls import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app