import logging
import time
import json
import random
from models import User

class UTCFormatter(logging.Formatter):
    """
    Formatter that forces timestamps to UTC instead of local time
    and formats output as structured JSON, including exceptions.
    """

    def __init__(self):
        super().__init__()

        # Force UTC timestamps
        self.converter = time.gmtime

    def format(self, record):
        """
        Convert LogRecord into JSON string with UTC timestamp.
        """

        # UTC ISO-8601 timestamp
        timestamp = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ",
            self.converter(record.created)
        )

        log_entry = {
            "timestamp": timestamp,
            "logger": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
            "file": record.pathname,
            "line": record.lineno
        }

        # Include exception information if present
        if record.exc_info:
            log_entry["exception"] = self.formatException(
                record.exc_info
            )

        # Include stack info if present
        if record.stack_info:
            log_entry["stack"] = self.formatStack(
                record.stack_info
            )

        return json.dumps(log_entry)


def spawn_user():
    user_names = ['ahmed', 'mohamed', 'jack', 'jones', 'jan', 'david', 'myers', 'doe', 'salma', 'salama', 'mike', 'ming', 'ding']
    first_name, last_name = user_names[random.randint(0, len(user_names))], user_names[random.randint(0, len(user_names))]
    user_name = first_name + ' ' + last_name
    email = first_name + '.' + last_name + '@example.org'
    orders = []
    balance = 3000 * (0.25 + random.random()*0.75)

    return User(user_name, email, orders, balance)
