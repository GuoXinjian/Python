from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///D:/Python/PUBGInFoRecognizewithOpenCV/data.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)

class KPL(db.Model):
    __tablename__ = 'KPL'
    id=db.Column(db.Integer,primary_key=True)

    bluedragon=db.Column(db.Integer)
    bluetower=db.Column(db.Integer)
    bluepoint=db.Column(db.Integer)
    reddragon=db.Column(db.Integer)
    redtower=db.Column(db.Integer)
    redpoint=db.Column(db.Integer)

    blueall=db.Column(db.Integer)
    redall=db.Column(db.Integer)

    # b10=pic[230:268,760:860]
    b1=db.Column(db.Integer)
    b2=db.Column(db.Integer)
    b3=db.Column(db.Integer)
    b4=db.Column(db.Integer)
    b5=db.Column(db.Integer)

    # r0=pic[230:268,1100:1200]
    r1=db.Column(db.Integer)
    r2=db.Column(db.Integer)
    r3=db.Column(db.Integer)
    r4=db.Column(db.Integer)
    r5=db.Column(db.Integer)
    
    def __repr__(self):
        return 'KPL MODEL'

@app.route('/')
def index():
    return str(KPL.query.order_by(KPL.id.desc()).first().__dict__)

if __name__=='__main__':

    db.drop_all()
    db.create_all()
    app.run('0.0.0.0',debug=True)

    # db.create_all()