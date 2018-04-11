from bottle import Bottle, static_file, jinja2_view
from wtforms import StringField, Form, DateTimeField, SubmitField

app = Bottle()


class TodoForm(Form):
    """WTFoms class to create simple components."""
    task = StringField('Task')
    date = DateTimeField('When', format='%Y-%m-%d')
    butt = SubmitField('ok')
    butt_s = SubmitField('show tasks')  # simplify js tests


@app.route('/static/:path#.+#')
def send_static(path):
    """Route to get static files like css and js files."""
    return static_file(path, root='static')


@app.route('/')
@jinja2_view('home.tpl', template_lookup=['views'])
def index():
    """View to render /."""
    return {'form': TodoForm()}
