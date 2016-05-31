from flask import Flask, render_template, json, request
import fileinput
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

    homepage = open("templates/index.html", "r")                                                           
    contents = homepage.readlines()                                                                            
    homepage.close() 
    
    entry_hash = return_entry(_title, contents)

    '''homepage = open("test_file", 'a')
    homepage.write("<!--" + entry_hash["entry"] + "-->")
    homepage.close'''
    
    homepage = open("test_file", 'a')
    homepage.write("<!--" + entry_hash["entry"] + "-->")
    homepage.close

    return json.dumps({'html':'<span>All fields good!</span>'})

if __name__ == "__main__":
    app.run()

def return_entry(title, contents):
    i = 1
    for line in contents:
        if '<table border="1">' in line:
            line = line.replace(line, line + '<tr class="entry_cell"><td class="img_cells"><a href="sample.txt"\><img src="http://img.pokemondb.net/sprites/black-white/normal/abra.png" alt="Abra"></a></td><td class="title"><a href="sample.txt">' + title + '</a></td><td class="timestamp">[timestamp]</td></tr>')
            return {'line': i, 'entry': line}
        i+=1
    return None
