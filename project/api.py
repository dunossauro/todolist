from bottle import Bottle, run
from front_end import app as front_app
from back_end import app as back_app


Routes = Bottle()
Routes.merge(front_app)
Routes.merge(back_app)

run(app=Routes, port=8080, debug=True, reloader=True)
