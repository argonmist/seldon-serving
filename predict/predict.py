import requests
import numpy as np
from PIL import Image
from proto import prediction_pb2
from matplotlib import pyplot as plt

API_AMBASSADOR = "172.23.128.50"

def load_image(filename):
    img = Image.open(filename)
    img.load()
    data = np.asarray(img, dtype='float32')
    data /= 255
    return data


def rest_request_ambassador(deploymentName,namespace,endpoint="localhost:8003",arr=None):
    shape = arr.shape
    payload = {"data":{"names":[], "tensor":{"shape":shape, "values":arr.tolist()}}}
    response = requests.post(
                "http://"+endpoint+"/seldon/"+namespace+"/"+deploymentName+"/api/v0.1/predictions",
                json=payload)
    print(response.status_code)
    print(response.text)

imgpath = './3300.png'
data = load_image(imgpath).flatten()
data = data.reshape((784))
rest_request_ambassador("mnist", "seldon-app", endpoint=API_AMBASSADOR, arr=data)
