from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URL'] = 'sqlite:///blog.db'
db=SQLAlchemy(app)


class Katalog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    price = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return '<Katalog %r>' % self.id




@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pronas')
def pronas():
    return render_template("pronas.html")


if __name__ == '__main__':
    app.run(debug=True)


