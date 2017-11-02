from flask import Flask, render_template, request, send_from_directory
import os
import urllib

app = Flask(__name__)

PORT = '8888'
UPLOAD = 'uploads'


@app.route('/')
def index():
    return render_template("index.html",
                           title='ResNet50 Classification Demo')


@app.route('/download', methods=['POST'])
def download_image():
    address = request.form['address']
    filename = os.path.join(UPLOAD, address.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(urllib.urlopen(address).read())
    return predict(filename)


@app.route('/upload', methods=['POST'])
def upload_image():
    f = request.files['image']
    filename = os.path.join(UPLOAD, f.filename)
    f.save(filename)
    return predict(filename)


@app.route('/' + UPLOAD + '/<path:path>')
def serve_files(path):
    return send_from_directory(UPLOAD, path)


def predict(filename):
    return render_template('predict.html', filename=filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
