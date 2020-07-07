from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("calendar.html")

@app.route('/receiver', methods=['GET'])
def date():
    clicked_date = request.get_json()
    print(clicked_date)
    return clicked_date

if __name__=='__main__':
    app.run(debug=True)