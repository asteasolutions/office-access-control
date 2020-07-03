from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def chess():
    return "Hello world"

if __name__=='__main__':
    app.run(debug=True)