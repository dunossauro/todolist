from json import dumps
from bottle import Bottle, static_file, jinja2_view, request
from wtforms import StringField, Form, DateTimeField, SubmitField

app = Bottle()


class TodoForm(Form):
    task = StringField('Task')
    date = DateTimeField('When', format='%y-%m/%d')
    butt = SubmitField('ok')


@app.route('/static/:path#.+#')
def send_static(path):
    return static_file(path, root='static')


@app.route('/')
@jinja2_view('home.tpl', template_lookup=['views'])
def index():
    return {'form': TodoForm(), 'xxx': 'oi'}


# --------------
# Service routes
# --------------


@app.route('/fetch')
def xx():
    """TODO: return SQLAlchemy json."""
    return dumps({'xxx': 'oi'})


@app.post('/fetchp')
def xx():
    print(request.json)
    return dumps({})


app.run()
