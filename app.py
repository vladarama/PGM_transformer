import os
import glob
import processing as pro
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename



# Only accepting PGM files
ALLOWED_EXTENSIONS = set(['pgm', 'compressed'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)

@app.route('/', methods = ['GET', "POST"])
@app.route('/home', methods = ['GET', "POST"])
def home():
    return render_template('index.html')


def remove_files():
    in_files = glob.glob('input/*')
    out_files = glob.glob('output/*')

    for f in in_files:
        os.remove(f)

    for f in out_files:
        os.remove(f)


@app.route('/invert', methods=['GET', 'POST'])
def invert():

    remove_files()

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join('input', filename)
            output_location = os.path.join('output', filename)
            file.save(save_location)

            pro.save_image(pro.invert(pro.load_image(save_location)), str('output/')+'new'+filename)
            return send_from_directory('output', 'new'+filename)

        return render_template('confirmation.html')

    return render_template('invert.html')




@app.route('/flip_horizontal', methods=['GET', 'POST'])
def flip_horizontal():

    remove_files()

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join('input', filename)
            file.save(save_location)

            pro.save_image(pro.flip_horizontal(pro.load_image(save_location)), str('output/')+'new'+filename)
            return send_from_directory('output', 'new'+filename)

        os.remove('input/'+filename)
        os.remove('output/'+'new'+filename)
        return render_template('confirmation.html')
    return render_template('flip_horizontal.html')


@app.route('/flip_vertical', methods=['GET', 'POST'])
def flip_vertical():

    remove_files()

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join('input', filename)
            file.save(save_location)

            pro.save_image(pro.flip_vertical(pro.load_image(save_location)), str('output/')+'new'+filename)
            return send_from_directory('output', 'new'+filename)
            
        os.remove('input/'+filename)
        os.remove('output/'+'new'+filename)
        return render_template('confirmation.html')
    return render_template('flip_vertical.html')

