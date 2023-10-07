import os


SECRET_TOKEN = "SECRET_TOKEN"
MAX_WEBHOOK_DELAY = "MAX_WEBHOOK_DELAY"
MAX_POLL_DELAY = "MAX_POLL_DELAY"
SUCCESS_RATE = "SUCCESS_RATE"


def get_secret_token():
    return os.getenv(SECRET_TOKEN)


def get_webhook_delay():
    return int(os.getenv(MAX_WEBHOOK_DELAY, "120"))


def get_poll_delay():
    return int(os.getenv(MAX_POLL_DELAY, "30"))


def get_success_rate():
    return int(os.getenv(SUCCESS_RATE, "50")) / 100


def set_env_var(key, value):
    os.environ[key] = str(value)
