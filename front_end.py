from bottle import Bottle, static_file, jinja2_view
from wtforms import StringField, Form, DateTimeField, SubmitField

app = Bottle()


class TodoForm(Form):
    task = StringField('Task')
    date = DateTimeField('When', format='%Y-%m-%d')
    butt = SubmitField('ok')
    butt_s = SubmitField('show tasks')  # simplify js tests


@app.route('/static/:path#.+#')
def send_static(path):
    return static_file(path, root='static')


@app.route('/')
@jinja2_view('home.tpl', template_lookup=['views'])
def index():
    return {'form': TodoForm()}
