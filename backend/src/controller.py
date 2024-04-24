import random
from flask import Flask, request
from flask_cors import CORS
import json
import service

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    disasterFile = request.files['file']
    disasterFileId = random.randint(0, 1000000)
    fileName = f'./disasterImages/disaster-{disasterFileId}.jpg'
    disasterFile.save(fileName)
    disaster = service.predictDisaster(fileName)
    return json.dumps({
        'id': disasterFileId,
        'disaster': disaster
    })

if __name__ == '__main__':
    app.run(port=8000, debug=True)