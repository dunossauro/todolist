from datetime import datetime
from json import dumps
from bottle import Bottle, request
from sqlalchemy import select
from db import engine, task_table

app = Bottle()
conn = engine.connect()
ins = task_table.insert()


@app.route('/fetch')
def xx():
    return dumps(
        [{'task': x[1], 'date': str(x[2])}
         for x in select([task_table]).execute()]
    )


@app.post('/fetchp')
def insert_db():
    returned = request.json
    if returned.keys():
        task = returned['task']
        date = datetime.strptime(returned['date'], '%Y-%m-%d')
        new_task = ins.values(task=task, date=date)
        conn.execute(new_task)
        return dumps({'OK': 200})
    return dumps({'error': 300})
