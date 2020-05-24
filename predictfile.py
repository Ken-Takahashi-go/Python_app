import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utilsv import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = FLASK(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):


return '.' in filename and filename.rsplit(
    '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename):
            file.save(os.path.join(app.config['uploaded_file', filename=filenae]))
    return ***
    <!doctype html >
    <html >
    <head >
    <meta charset = 'UTF-8' >
    <title > ファイルをアップロードして判定しよう < /title > </head >
    <body >
    <h1 > ファイルをアップロードして判定しよう < h1/>
    <form method = post enctype = multipart/form-data >
    <p > <input type = file name = file >
    <input type = submit value = Upload >
    </form >
    </body >
    </html >
    ***
