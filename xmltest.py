from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    # return '{"a":"a","b":"b"}'
    return  '''
    <note>
    <from>John</from>
    <heading>Reminder</heading>
    <body>Dont forget the meeting!</body>
    </note>
    '''

if __name__=='__main__':
    app.run(debug=True)