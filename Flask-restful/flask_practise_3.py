#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
	{
		'id': 1,
		'title': u'Bug groceries',
		'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
		'done':False
	},
	{
		'id': 2,
		'title': u'learn python',
		'description':u'Need to find a good python tutorial on the web',
		'done': False
	}
]

# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_task():
# 	return jsonify({'task': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task[0]})


if __name__ == '__main__':
	app.run(debug=True)

