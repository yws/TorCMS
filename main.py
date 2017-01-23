from flask import Flask
from flask import render_template
from flask import render_template_string

from torcms.model.post_model import MPost

from flask_wtf import CSRFProtect

from flasky import create_app

app = create_app('default')


CSRFProtect(app)
# CsrfProtect(app)


@app.context_processor
def inject_user():
    return dict(test="<h1>a tmp variable</h1>")

#下面的functest函数也是可以在所有的模板中使用的
#使用方式如下{{ functionname(参数) }}
@app.context_processor
def testfunc():
    def post_recent(**kwargs):
        # return "{0}".format(kwargs)

        mpost = MPost()
        recs = mpost.query_recent_most(kwargs['num'])
        kwd = {
        }
        #     'with_date': with_date,
        #     'with_catalog': with_catalog,
        #     'router': router_post['1'],
        # }
        # return  'Hee'
        return render_template('modules/post/post_list.html', recs=recs, kwd=kwd)

    return dict(post_recent=post_recent)
# app = Flask(__name__)


#
#
# class post_recent_most_view(tornado.web.UIModule):
#     def render(self, num, recent, with_date=True, with_catalog=True):
#         self.mpost = MPost()
#         recs = self.mpost.query_recent_most(num, recent)
#         kwd = {
#             'with_date': with_date,
#             'with_catalog': with_catalog,
#             'router': router_post['1'],
#         }
#         return self.render_string('modules/post/post_list.html', recs=recs, kwd=kwd)
#


app.config['SECRET_KEY'] = 'hard to guess string'
app.config['CSRF_KEY'] = 'hard to guess string'
app.config['CSRF'] = 'hard to guess string'

if __name__ == '__main__':
    print(app.template_folder)
    app.run(debug=True, host='0.0.0.0')

    # app.run()
