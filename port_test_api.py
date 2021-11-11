import os

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

#Baseline
@app.route("/")
def index():
    return make_response({"data":"Welcome to Port Checker"}, 200)

#listagem de task
tasks = [{'id':1,
          'title':'Check port status',
          'desc':'Lista o fluxo de informacao recente de saida ou entrada de uma dada porta'},
        {'id':2,
          'title':'Check all ports',
          'desc':'Gera listagem de todas as portas'}]

#Task lista todas as tasks disponiveis
@app.route("/tasks")
def list_tasks():
    return make_response(jsonify({"tasks":tasks}), 200)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error":"not found"}), 404)

@app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task = [x for x in tasks if x['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return make_response(jsonify({"task":task[0]}), 200)


@app.route('/tasks/1/<port>',methods=['GET'])
def list_port(port):
    print(port)
    netstat_check = os.popen('netstat -na | find "{}" '.format(port)).read()
    #Gera uma resposta com base nisso
    return make_response(jsonify({"task":netstat_check}), 200)

if __name__ == '__main__':
    print("API starting")
    app.run(host = 'localhost', port=5000)
    print("API closing")

#codigo sem ser apirest
"""
user_input = 1
while user_input > 0:
    user_input = input("Digite a porta a ser checada, ou -1 para sair: ")
    if user_input == "-1":
        print("Adeus")
        break
    try:
        user_input = int(user_input)
    except:
        print("Valor de porta invalido. Favor inserir outro valor:")
        continue
    output = os.popen('netstat -na | find "{}" '.format(user_input)).read()
    print(output)
"""