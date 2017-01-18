from flask import Flask
from flask import render_template

from flasky import create_app

app = create_app('default')


# app = Flask(__name__)







if __name__ == '__main__':
    print(app.template_folder)
    app.run(debug=True, host='0.0.0.0')

    # app.run()
