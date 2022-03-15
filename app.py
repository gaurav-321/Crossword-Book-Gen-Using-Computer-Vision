import random
import shutil
from glob import glob
from flask import Flask, render_template, request, redirect, send_file
from main import main
import os
from os.path import join, dirname, realpath

app = Flask(__name__)
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

try:
    shutil.rmtree("static/files")
    os.makedirs("static/files")
    shutil.rmtree("static/back")
    os.makedirs("static/files")
except:
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html', fonts=glob("fonts/*.ttf"))
    else:
        data = request.form.to_dict()
        bold_header = "bold_header" in request.form
        bold_word = "bold_word" in request.form
        paging_enable = "paging_enable" in request.form
        print(data, bold_header, bold_word, paging_enable)
        uploaded_file = request.files['csv_file']
        csv_rand_file = f"{random.randint(1, 100000)}.csv"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_rand_file)
        uploaded_file.save(file_path)
        files = request.files.getlist("media[]")
        print(files)
        back_images = []
        for file in files:
            filename = f"{random.randint(1,1000000)}.{file.filename.split('.')[-1]}"
            if file.filename:
                file.save(os.path.join("background", filename))
                back_images.append("background/"+filename)
        main(csv_file=file_path,
             BACKGROUND_IMAGES=random.choice(back_images) if len(back_images) > 0 else [],
             font=data['font_name'],
             header_bold=1 if bold_header else 0, header_size=int(data['header_size']),
             header_color=tuple(int(x) for x in data['header_color'].split(",")),
             pagination_write=paging_enable,
             font_size=int(data['word_size']), word_bold=1 if bold_word else 0)
        return send_file("static/output/output.pdf", download_name='output.pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
