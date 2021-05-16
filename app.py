# from flask import Flask,render_template,request
# from flask_sqlalchemy import SQLAlchemy
#
#
# app = Flask(__name__)
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#
#
# @app.route('/')
# def base():
#     return render_template("base.html")
#
# db=SQLAlchemy(app)
#
#
# class Katalog_1(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(30),nullable=False)
#     price = db.Column(db.Integer,nullable=False)
#
#     def __repr__(self):
#         return '<katalog_1 %r>' % self.id
#
#
# @app.route('/form',methods=('POST','GET'))
# def form_admin():
#     if request.method=="POST":
#         try:
#             animal=Katalog_1(name=request.form['name'],price=request.form['price'])
#             db.session.add(animal)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             print("Ошибка введения банных в базу")
#
#     return render_template("form.html")
#
#
#
#
#
#
#
# @app.route('/pronas')
# def pronas():
#     return render_template("pronas.html")
#
#
# @app.route('/katalog')
# def katalog():
#     return render_template("katalog.html")
#
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test2.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



@app.route('/')
def test():
    return render_template('base.html', title="TEsT title")


db = SQLAlchemy(app)


class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)

    def __init__(self,name,price):
        self.name = name
        self.price = price
    def repr(self):
        return f"<animal {self.name}>"



@app.route("/form", methods=("POST", "GET"))
def admin():
    if request.method == "POST":
        name_new = request.form['name']
        price_new = request.form['price']
        name_old = request.form['name_1']
        price_renewed = request.form['price_2']


        if name_new != '' and price_new != '':
            try:
              animal = Animals(name=name_new, price=price_new)
              db.session.add(animal)
            # db.session.flush()
              db.session.commit()
            except:
              db.session.rollback()
            print("Database adding Error")
        else :
            try:
                old_object = Animals.query.filter_by(name=name_old).first()
                print(old_object)
                old_object.price = price_renewed

                db.session.commit()

            except:
                db.session.rollback()
                print("Change is falend")


    return render_template('form.html')

@app.route('/show')
def show():
    date = Animals.query.filter_by(name="cat_1").first()
    print(date)
    return render_template("show.html",cat=date)



@app.route('/katalog_1')
def katakog_1():
    prices = {'cat': Animals.query.filter_by(name="cat").first().price,
               'cat_1':Animals.query.filter_by(name="cat_1").first().price}

    return render_template("katalog_1.html",date=prices)


@app.route('/katalog')
def katalog():
    return render_template("katalog.html")


@app.route('/pronas')
def pronas():
    return render_template("pronas.html")

if __name__ == 'main':
    db.create_all()
    app.run(debug=True)



