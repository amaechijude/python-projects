from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/hello')
def hello_page():
    return "Hello People"

if __name__  == '__main__':
    app.run(debug=True)
