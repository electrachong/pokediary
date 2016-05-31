from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/create_entry_form",methods=['POST', 'GET'])
def create_entry_form():
    return render_template('create_entry_form.html')

@app.route('/create_entry',methods=['POST', 'GET'])
def create_entry():
    _title = request.form['title']
    _filetype = request.form['filetype']
    _body = request.form['bodytext']

    return "ttest2"

if __name__ == "__main__":
    app.run()
