from flask import Flask, request, jsonify

app = Flask(__name__)
toDOlist = []
toDoItem = {}
toDoItem['name'] = "Flask"
toDoItem['priority'] = 3
toDOlist.append(toDoItem)
toDOlist.append(toDoItem)
toDOlist.append(toDoItem)


@app.route('/')
def get_status():  # put application's code here
    status = ""
    for item in toDOlist:
        status += f"name: {item['name']}   &nbsp; &nbsp; " \
                  f" priority: {item['priority']}  </br> "
    return status


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/get/<id>')
def getToDO(id):
    if 0 <= int(id) < len(toDOlist):
        item=toDOlist[int(id)]
        return f"name: {item['name']}   &nbsp; &nbsp; " \
                  f" priority: {item['priority']}  </br> "
    else:
        return jsonify(toDOlist)
        return "Not Found"

@app.route('/set', methods=['POST'])
def foo():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run()
