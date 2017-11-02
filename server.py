from flask import Flask, render_template, request
app = Flask(__name__)

PORT = '8888'

@app.route('/')
def index():
    return render_template("index.html",
                           title='ResNet50 Classification Demo')

@app.route('/predict', methods=['POST'])
def predict():
    address = request.form['address']
    return render_template("predict.html", url_address=address)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
