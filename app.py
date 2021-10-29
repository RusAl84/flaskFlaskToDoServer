from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

# https://docs-python.ru/packages/veb-frejmvork-flask-python/registratsija-marshrutov-url-adresov-flask/
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/get/<id>')
def getToDO(id):
    if 0 <= int(id) < len(toDOlist):
        item=toDOlist[int(id)]
        # return f"name: {item['name']}   &nbsp; &nbsp; " \
        #           f" priority: {item['priority']}  </br> "
        return jsonify(item)
    else:
        return jsonify(toDOlist)
        return "Not Found"

@app.route('/set', methods=['POST'])
def foo():
    data = request.json
    print(data)
    toDOlist.append(data)

    # return jsonify(data)
    return f"## Add {data}", 200, {'Content-Type': 'text/markdown'}
if __name__ == '__main__':
    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')