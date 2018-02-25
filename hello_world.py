from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World!' + '\n' + 'My name is Pete'

app.run(debug=True)