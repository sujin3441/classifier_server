from flask import Flask, render_template
app = Flask(__name__)

PORT = '8888'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Hara'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
