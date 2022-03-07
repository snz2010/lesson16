import raw_data
from models import User, Offer, Order


def input_data(db):
    # 2 - заполним поля таблиц значениями из словаря 1
    for user_data in raw_data.users:
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
    # 2 - заполним поля таблиц значениями из словаря 2
    for offer_data in raw_data.offers:
        new_offer = Offer(
            id=offer_data["id"],
            order_id=offer_data["order_id"],
            executor_id=offer_data["executor_id"],
        )
        db.session.add(new_offer)
        db.session.commit()
    # 2 - заполним поля таблиц значениями из словаря 3
    for order_data in raw_data.orders:
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
