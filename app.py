import json

import create_data
from setup_db import db
from flask import Flask, request, jsonify

from models import User, Order, Offer
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
with app.app_context():
    db.create_all()
    # 1 - создаем описанные таблицы
    create_data.input_data(db)
app.debug = True


@app.route('/users', methods=["POST", "GET"])
def all_users():
    # 3 - прописываем РУТЫ для получения всех пользователей /users ...
    if request.method == "GET":
        res = []
        for u in User.query.all():
            res.append(u.to_dict())
        return jsonify(res), 200

    # 6 - создание пользователя user посредством метода POST на URL /users
    elif request.method == "POST":
        user_data = json.loads(request.data)
        # Можно данные брать из словаря form: user_data = request.form
        new_user = User(
            id=user_data["id"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            age=user_data["age"],
            email=user_data["email"],
            role=user_data["role"],
            phone=user_data["phone"],
        )
        db.session.add(new_user)
        db.session.commit()
        return "", 201


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user(uid: int):
    # 3 - ... и для одного пользователя по идентификатору /users/1
    if request.method == "GET":
        return jsonify(User.query.get(uid).to_dict()), 200

    # 6 - удаление пользователя user посредством метода DELETE на URL /users/<id>
    elif request.method == "DELETE":
        u = User.query.get(uid)
        db.session.delete(u)
        db.session.commit()
        return "", 204
    # 6 - обновление пользователя user посредством метода PUT на URL /users/<id>
    elif request.method == "PUT":
        user_data = json.loads(request.data)
        u = User.query.get(uid)
        u.first_name = user_data["first_name"]
        u.last_name = user_data["last_name"]
        u.age = user_data["age"]
        u.email = user_data["email"]
        u.role = user_data["role"]
        u.phone = user_data["phone"]
        db.session.add(u)
        db.session.commit()
        return "", 204


@app.route('/orders', methods=["POST", "GET"])
def all_orders():
    # 4 - представление для заказов, которое обрабатывало бы GET-запросы получения всех заказов /orders ...
    if request.method == "GET":
        res = []
        for o in Order.query.all():
            res.append(o.to_dict())
        return jsonify(res), 200

    # 7 - создание заказа order посредством метода POST на URL /orders
    elif request.method == "POST":
        order_data = json.loads(request.data)
        new_order = Order(
            id=order_data["id"],
            name=order_data["name"],
            description=order_data["description"],
            start_date=order_data["start_date"],
            end_date=order_data["end_date"],
            address=order_data["address"],
            price=order_data["price"],
            customer_id=order_data["customer_id"],
            executor_id=order_data["executor_id"],
        )
        db.session.add(new_order)
        db.session.commit()
        return "", 201


@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def order(uid: int):
    # 4 - ... и для одного заказа по идентификатору /orders/1
    if request.method == "GET":
        return jsonify(Order.query.get(uid).to_dict()), 200

    # 7 - удаление заказа order посредством метода DELETE на URL /orders/<id>
    elif request.method == "DELETE":
        o = Order.query.get(uid)
        db.session.delete(o)
        db.session.commit()
        return "", 204
    # 7 - обновление заказа order посредством метода PUT на URL /orders/<id>
    elif request.method == "PUT":
        order_data = json.loads(request.data)
        o = Order.query.get(uid)
        o.description = order_data["description"]
        o.start_date = order_data["start_date"]
        o.end_date = order_data["end_date"]
        o.address = order_data["address"]
        o.price = order_data["price"]
        o.customer_id = order_data["customer_id"]
        o.executor_id = order_data["executor_id"]
        db.session.add(o)
        db.session.commit()
        return "", 204


@app.route('/offers', methods=["POST", "GET"])
def all_offers():
    # 5 - представление для предложений, которое обрабатывало бы GET-запросы получения всех предложений /offers ...
    if request.method == "GET":
        res = []
        for u in Offer.query.all():
            res.append(u.to_dict())
        return jsonify(res), 200

    # 8 - создание предложения offer посредством метода POST на URL /offers
    elif request.method == "POST":
        offer_data = json.loads(request.data)
        new_offer = Offer(
            id=offer_data["id"],
            order_id=offer_data["order_id"],
            executor_id=offer_data["executor_id"],
        )
        db.session.add(new_offer)
        db.session.commit()
        return "", 201


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def offer(uid: int):
    # 5 - ... и предложения по идентификатору /offers/<id>
    if request.method == "GET":
        return jsonify(Offer.query.get(uid).to_dict()), 200

    # 8 - обновление предложения offer посредством метода PUT на URL /offers/<id>
    elif request.method == "PUT":
        offer_data = json.loads(request.data)
        o = Offer.query.get(uid)
        # o.id = offer_data["id"]
        o.order_id = offer_data["order_id"]
        o.executor_id = offer_data["executor_id"]
        db.session.add(o)
        db.session.commit()
        return "", 204
    # 8 - удаление предложения offer посредством метода DELETE на URL /offers/<id>
    elif request.method == "DELETE":
        o = Offer.query.get(uid)
        db.session.delete(o)
        db.session.commit()
        return "", 204


if __name__ == '__main__':
    app.run()
