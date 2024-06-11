import os

def get_welcome_message():
    return os.getenv("WELCOME_MESSAGE", "Hello, World!")
