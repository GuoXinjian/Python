from flask import Flask,request


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index(): 
    if request.method   == 'GET':
        return 'GET'
    elif request.method == 'POST':
        return 'POST'

if __name__=='__main__':
    app.run()
