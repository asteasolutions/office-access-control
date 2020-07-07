from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("calendar.html")

@app.route('/date', methods=['GET'])
def date():
    clicked_date = request.get_json()
    print(clicked_date)
    return render_template("day.html")

@app.route('/real_time', methods=['GET', 'POST'])
def real_time():
    return render_template("real_time.html", event_date = "03.33.33")

if __name__=='__main__':
    app.run(debug=True)