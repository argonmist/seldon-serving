import os
from flask import request, abort, Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/model/deploy', methods=['POST'])
def deploy():
    if not request.json:
        abort(400)

    dname = request.json['deployname']
    mname = request.json['modelname']
    cmd = "helm install ./seldon-single-model --name " + dname + " --set model.env.MODEL_NAME=" + mname + " --namespace seldon-app"
    subprocess.call(cmd.split())
    return "Deploy Success" 

@app.route('/model/delete', methods=['POST'])
def delete():
    if not request.json:
        abort(400)

    dname = request.json['deployname']
    cmd = "helm del --purge " + dname
    subprocess.call(cmd.split())
    return "Delete Success"

@app.route('/model/list', methods=['GET'])
def list():
    dpname = []
    cmd = "helm list --namespace seldon-app | grep DEPLOYED"
    result = str(subprocess.check_output(cmd.split()), encoding='utf-8')
    result = result.splitlines()
    for i in range(len(result)):
        result[i] = result[i].split( )    
        if i > 0:
            dpname.append(result[i][0])
    keys=['deployname']
    d = dict.fromkeys(keys, dpname)
    return jsonify(d)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
