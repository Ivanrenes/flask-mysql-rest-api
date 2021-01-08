from app import app, jsonify, request, db,  ma
from app.models import Task, task_schema, tasks_schema



@app.route('/tasks', methods=['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)

@app.route('/tasks', methods=['GET'])
def getTasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)

@app.route('/tasks/<id>', methods=['GET'])
def getTask(id):
    task = Task.query.get(id)
    result = task_schema.dump(task)
    return jsonify(result)

@app.route('/tasks/<id>', methods=['PUT'])
def updateTask(id):
    task = Task.query.get(id)

    title = request.json['title']
    description = request.json['description']

    task.title = title
    task.description = description

    db.session.commit()
    return task_schema.jsonify(task)

@app.route('/tasks/<id>', methods=['DELETE'])
def deleteTask(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return task_schema.jsonify(task);

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message from 1v4nC0d3" : "Welcome to my API!",
        "routes":"/tasks/",
        "methods":"POST, PUT, DELETE, GET",
        "type":"JSON",
        "data_structure":"title, description"
    })