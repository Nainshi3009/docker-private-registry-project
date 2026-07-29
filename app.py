from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World 12345'

app.run(host="0.0.0.0", port=6000)