import logging
import logging.config
import json
import services
import models
import random

def configure_loggers():
    # load json configuration file
    with open("./configs/logging_config.json", 'r') as f:
        config_dict = json.load(f)
    logging.config.dictConfig(config_dict)

def load_services():
    inventory = models.Inventory("./data/inventory.json", "./data/product_details.json")
    inventory_service = services.InventoryService(inventory)

    user_service = services.UserService("./data/users.json")
    return inventory, inventory_service, user_service


def main():
    invnetory, inventory_service, user_service = load_services()

    while True:
        user = user_service.get_user(random.randint(0, len(user_service.total_user_no)))
        inventory_service.stock[]
if __name__ == "__main__":
    main()