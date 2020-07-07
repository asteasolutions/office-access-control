from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT']
clicked_date = ""

@app.route('/', methods=['GET'])
def main():
    return render_template("calendar.html")

@app.route('/date', methods=['GET'])
def date():
    clicked_date = request.args['res']
    print(clicked_date)
    return render_template("day.html", date=clicked_date)

if __name__=='__main__':
    app.run(debug=True)