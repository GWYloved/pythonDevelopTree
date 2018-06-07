from flask import Flask,abort
import datetime
import time
app = Flask(__name__)

@app.route('/')
def index():
	return  'Hello, world'

@app.route('/gg')
def gg():
	return  'gg'

@app.route('/time')
def ti():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/404')
def err_404():
	abort(404)

@app.route('/300')
def err_300():
	abort(300)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
