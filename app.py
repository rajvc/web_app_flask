
from flask import Flask

app = Flask(__name__)


from flask import render_template

@app.route('/')
def hello():
    return render_template('Home.html')

@app.route('/Login')
def login():
    return render_template('page.html')

if __name__ == '__main__':
    app.run()
