#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries= []

    for bakery in Bakery.query.all():
        bakery_dict ={
            "id" : bakery.id,
            "created_at": bakery.created_at,
            "name" : bakery.name,
            "updated_at" : bakery.updated_at,
        }

        bakeries.append(bakery_dict)

    response = make_response(jsonify(
         bakeries),
        200,
        {'Content-Type': 'application/json'}
    )

    return response


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()

    bakery_dict = bakery.to_dict()
    response = make_response(
        jsonify(bakery_dict),
        200,
        {'Content-Type': 'application/json'}
    )
    return response



@app.route('/baked_goods/by_price')
@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = []
    for baked_good in BakedGood.query.order_by(BakedGood.price).all():
        baked_good_dict = {
            'name' : baked_good.name,
            'price' : baked_good.price,
            'updated_at': baked_good.updated_at,
            'created_at': baked_good.created_at
        }

        baked_goods.append(baked_good_dict)

    response = make_response(
        jsonify(baked_goods),
        200,
        {"Content-Type" : "application/json"}
    )

    return response



@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    max_baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()

    max_baked_good_serialized = max_baked_good.to_dict()

    response = make_response(
        jsonify(max_baked_good_serialized),
        200,
    )

    return response




if __name__ == '__main__':
    app.run(port=5555, debug=True)
