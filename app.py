
import loadTest
from flask import Flask
from flask import jsonify
from flask import request
from numpy import loadtxt
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Request'

@app.route('/memoryLoad', methods=['POST'])
def memoryLoad():
    data = request.json
    target = data['target']
    loadTest.memory_generator(target)
    return 'Memory Generating...'

@app.route('/cpuLoad', methods=['POST'])
def cpuLoad():
    data = request.json
    target, durations, options, core = data['target'], data['durations'], data['options'], data['core']
    loadTest.cpu_generator(target, durations, options, core)
    return 'CPU Load Generating...'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)