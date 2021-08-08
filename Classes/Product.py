from header import *


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    barcode = db.Column(db.String(100))
    unitPrice = db.Column(db.String(100))
    sellPrice = db.Column(db.String(100))
    qty = db.Column(db.String(100))

    @staticmethod
    def Index():
        db.create_all()
        message = {"message": "Table Created"}
        return jsonify(message)

    @staticmethod
    def GetProductAll():
        __tablename__ = "product"
        objProduct = Product.query.all()
        result = []
        for col in objProduct:
            product_dict = {}
            product_dict["id"] = col.id
            product_dict["name"] = col.name
            product_dict["barcode"] = col.barcode
            product_dict["unitPrice"] = col.unitPrice
            product_dict["sellPrice"] = col.sellPrice
            product_dict["qty"] = col.qty
            result.append(product_dict)
        return json.dumps(result)

    @staticmethod
    def CreateProduct():
        data = request.get_json()
        objProduct = Product()
        objProduct.name = data['name']
        objProduct.barcode = data['barcode']
        objProduct.unitPrice = data['unitPrice']
        objProduct.sellPrice = data['sellPrice']
        objProduct.qty = data['qty']
        db.session.add(objProduct)
        message = {"message": "User Created"}
        db.session.commit()
        return jsonify(message)

    @staticmethod
    def deleteProductByPublicId(id):
        objUser = Product.query.filter_by(id=id).first()

        if not objUser:
            return jsonify({"message": "No user found"})
        db.session.delete(objUser)
        db.session.commit()
        return "User has been deleted"

    @staticmethod
    def SearchProductByName():
        data = request.get_json()
        objUser = Product.query.filter_by(name=data['name'])
        if not objUser:
            message = {"message": "Not Found User"}
            return jsonify(message)
        result = []
        for col in objUser:
            rename_dict = {}
        rename_dict["id"] = col.id
        rename_dict["barcode"] = col.barcode
        rename_dict["sellPrice"] = col.sellPrice
        rename_dict["qty"] = col.qty
        result.append(rename_dict)
        return json.dumps(result)

    @staticmethod
    def updateProductById(id):
        try:
            if request.method == "PUT":
                objProduct = Product.query.filter_by(id=id).first()
                if not objProduct:
                    return jsonify({"message": "not found id=" + id})
                if objProduct:
                    objProduct
                    data = request.get_json()
                    objProduct.name = data['name']
                    objProduct.barcode = data['barcode']
                    objProduct.unitPrice = data['unitPrice']
                    objProduct.sellPrice = data['sellPrice']
                    objProduct.qty = data['qty']

                    db.session.add(objProduct)
                    db.session.commit()
                    return jsonify({"message:": "product update"})
        except Exception as ex:
            return jsonify({"message": "product updated"})

