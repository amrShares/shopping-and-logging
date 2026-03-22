import logging
import json
from models import User
from models import Cart

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, users_path):
        self._users_path = users_path
        self.load_user_data()
        self.total_user_no = len(self.__users)

    def load_user_data(self):
        try:
            with open(self._users_path, 'r') as f:
                self.__users = json.load(f)
            logger.info(f"Loaded user data from {self._users_path}")
        except FileNotFoundError:
            logger.exception(f"users file {self._users_path} not found. Starting with empty user base.")
            self.__users = {}

    def get_user_data(self, user_id):
        return self.__users.get(str(user_id), False)

    def get_user(self, user_id):
        return User(self.get_user_data(user_id)), Cart()

    def view_user_data(self, user_id):
        user_data = self.__users.get(str(user_id))

        if not user_data:
            logger.warning(f"User {user_id} not found")
            return

        print(User(**user_data))

    def add_user(self, user_data : User):
        if not isinstance(user_data, User):
            print('please provide a valid User')
            return False
        self.__users[str(len(self.__users)+1)] = user_data.as_dict()
        self.save_user_data()

    def save_user_data(self):
        try:
            with open(self._users_path, 'w') as f:
                json.dump(self.__users, f, indent=4)

            logger.info(
                f"User data saved to {self._users_path}"
            )

        except Exception:
            logger.exception(
                "Failed to save user data"
            )