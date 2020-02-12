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

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
