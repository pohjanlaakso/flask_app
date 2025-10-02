
from flask import Flask

app = Flask(__name__)

@app.route('/')
#def hello_world():
#    return 'Hello world Hello!'

def index():
    page_title = 'Dynamic Home Page'

if __name__ == '__main__':
    app.run(debug=True)