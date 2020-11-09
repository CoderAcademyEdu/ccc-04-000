import os

class Config(object):
    @property
    def MY_ENV(self):
        value = os.environ.get("MY_ENV")

        if not value:
            value = "Not Set"

        return value

app_config = Config()