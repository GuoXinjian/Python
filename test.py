from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello</p>'


app.run('0.0.0.0')