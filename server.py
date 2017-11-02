from flask import Flask, render_template, request
import os
import urllib

app = Flask(__name__)

PORT = '8888'
UPLOAD = 'uploads'

@app.route('/')
def index():
    return render_template("index.html",
                           title='ResNet50 Classification Demo')

@app.route('/predict', methods=['POST'])
def predict_url():
    address = request.form['address']
    filename = os.path.join(UPLOAD, address.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(urllib.urlopen(address).read())
    return render_template("predict.html", url_address=address)

@app.route('/upload', methods=['POST'])
def upload_image():
    f = request.files['image']
    filename = os.path.join(UPLOAD, f.filename)
    f.save(filename)
    return render_template("index.html",
                           title='ResNet50 Classification Demo')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
