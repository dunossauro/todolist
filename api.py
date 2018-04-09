from datetime import datetime
from json import dumps
from bottle import Bottle, static_file, jinja2_view, request
from wtforms import StringField, Form, DateTimeField, SubmitField
from sqlalchemy import select
from db import engine, task_table

app = Bottle()


class TodoForm(Form):
    task = StringField('Task')
    date = DateTimeField('When', format='%Y-%m-%d')
    butt = SubmitField('ok')


@app.route('/static/:path#.+#')
def send_static(path):
    return static_file(path, root='static')


@app.route('/')
@jinja2_view('home.tpl', template_lookup=['views'])
def index():
    return {'form': TodoForm()}


# --------------
# Service routes
# --------------

conn = engine.connect()
ins = task_table.insert()


@app.route('/fetch')
def xx():
    s = select([task_table])
    return dumps({x[1]: str(x[2]) for x in s.execute()})


@app.post('/fetchp')
def insert_db():
    returned = request.json
    # import pdb; pdb.set_trace()
    if returned.keys():
        new_task = ins.values(
            task=returned['task'],
            date=datetime.strptime(returned['date'], '%Y-%m-%d')
            )
        conn.execute(new_task)
        return dumps({'OK': 200})


app.run()
