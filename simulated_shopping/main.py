import logging
import logging.config
import json
import services
import models
import random
import time
import utils

from simulated_shopping.models import Order
from simulated_shopping.services import OrderService


def configure_loggers():
    # load json configuration file
    with open("./configs/logging_config.json", 'r') as f:
        config_dict = json.load(f)
    logging.config.dictConfig(config_dict)

def load_services():
    inventory = models.Inventory("./data/inventory.json", "./data/product_details.json")
    inventory_service = services.InventoryService(inventory)

    user_service = services.UserService("./data/users.json")
    order_service = OrderService(inventory_service)
    return inventory, inventory_service, user_service, order_service


def main():
    inventory, inventory_service, user_service, order_service = load_services()

    for i in range(100):
        create_user = random.random() > 0.95
        if create_user:
            new_user = utils.spawn_user()
            user_service.add_user(new_user)
            print('creating a new user with the details')
            print(new_user)

        user_id = random.randint(1, user_service.total_user_no)
        user, cart = user_service.get_user(user_id)
        products_to_buy = [random.randint(1, inventory.no_of_products), random.randint(1, inventory.no_of_products), random.randint(1, inventory.no_of_products)]
        print(user)

        print(f'will aim to buy the products:')
        for i in range(3):
            print(inventory.get_product_details(products_to_buy[i]))

        for product_id in products_to_buy:
            cart.add_item(product_id, random.randint(1, 3))

        user_order, total_price = order_service.create_order(user_id, user.available_balance(), cart, inventory)
        if not isinstance(user_order, models.Order):
            if total_price == 0:
                print('purchase was cancelled as one of the stock does not contain enough units of one of the products')
            else:
                print(f'the purchase (total price={total_price}) is greater than the available user balance')
        else:
            user_service.reduce_balance(user_id, total_price)
            print(f'the purchase(total price={total_price}) was completed')

        time.sleep(1)


if __name__ == "__main__":
    main()