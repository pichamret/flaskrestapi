from sqlalchemy import ForeignKey

from header import *

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(250),unique=True)
    # userId = db.Column(db.Interger)
    # createdAt = db.Column(db.DateTime,default=datetime.datetime.now())

    @staticmethod
    def Index():
        db.create_all()
        message = {"message": "Table Created"}
        return jsonify(message)

    @staticmethod
    def Index():
        db.create_all()
        message = {"message": "Table Created"}
        return jsonify(message)

    @staticmethod
    def createCategory():
        __tablename__ = "category"
        data = request.get_json()
        category = Category()
        category.categoryName = data['categoryName']
        db.session.add(category)
        message = {"message": "category Created"}
        db.session.commit()
        return jsonify(message)
