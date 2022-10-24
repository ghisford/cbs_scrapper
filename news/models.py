from news import db
from datetime import datetime

class ExtraMixin(object):
    article_id = db.Column(db.Integer,primary_key= True)
    added_at = db.Column(db.DateTime,default= datetime.utcnow())



    def save(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session()



class Article(db.Model,ExtraMixin):
    __tablename__ = 'cbs_news'
    title = db.Column(db.String(100),nullable= False)
    link = db.Column(db.String(100),nullable= False)
    image = db.Column(db.String(100))
    description = db.Column(db.String(100),nullable= False)


    @classmethod
    def get_all(cls):
        return cls.query.all()
