import os
import time
import sys
from dotenv import load_dotenv
load_dotenv()


def get_env(env_name: str, input_message: str):
    if env_name in os.environ:
        return os.environ[env_name]
    value = input(input_message)
    try:
        return value
    except ValueError as e:
        print(e, file=sys.stderr)
        time.sleep(1)
