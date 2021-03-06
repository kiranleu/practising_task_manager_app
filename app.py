import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World....Again"
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
    port=int(os.environ.get('PORT', '8080')),
    debug=True)