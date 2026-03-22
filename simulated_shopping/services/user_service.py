import logging
import json
from models import User

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, users_path):
        self._users_path = users_path
        self.load_user_data()

    def load_user_data(self):
        try:
            with open(self._users_path, 'r') as f:
                self.__users = json.load(f)
            logger.info(f"Loaded user data from {self._users_path}")
        except FileNotFoundError:
            logger.exception(f"users file {self._users_path} not found. Starting with empty user base.")
            self.__users = {}

    def view_users(self):
        return self.__users

    def get_user_data(self, user_id):
        return self.__users.get(user_id, False)

    def view_user_data(self, user_id):
        print(User(**self.__users[user_id]))