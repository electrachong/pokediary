# encoding: utf-8                                                                 

from flask import Flask, render_template, json, request
import fileinput
from string import Template

app = Flask(__name__)
dirpath = '/root/pokediary/entries/'
cell_template = Template("""<tr class="entry_cell"><td class="img_cells"><a href=\
"sample.txt"\><img src="http://img.pokemondb.net/sprites/black-white/normal/abra.\
png" alt="Abra"></a></td><td class="title"><a href="${relpath}">${title}</a></td>\
<td class="timestamp">[timestamp]</td></tr>""")

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

    full_path = dirpath + _title + _filetype
    newfile = open(full_path, 'w')
    newfile.write(_body)
    newfile.close()

    homepage = open("templates/index.html", "r")
    contents = homepage.readlines()
    homepage.close()

    homepage = open("templates/index.html", 'w')
    for line in contents:
        homepage.write(line)
        if '<table border="1">' in line:
            homepage.write(cell_template.substitute(relpath='entries/' + _title +\
 _filetype, title=_title))
    homepage.close()

    return json.dumps({'html':'<span>All fields good!</span>'})

@app.route('/entries/<filename>')
def find_page(filename):
    file = open(dirpath + filename, 'r')
    return file.read()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
