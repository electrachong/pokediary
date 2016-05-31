from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/create_entry_form")
def create_entry_form():
    return render_template('create_entry_form.html')


if __name__ == "__main__":
    app.run()
