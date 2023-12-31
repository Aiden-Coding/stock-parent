"""
Global Sanic Application Setting

See `.env` for default settings.
 """

import os


class Config(object):
    # If not set fall back to production for safety
    SANIC_ENV = os.getenv('SANIC_ENV', 'production')
    DEBUG = bool(os.getenv('DEBUG', False))
    # Set SANIC_SECRET on your production Environment
    SECRET_KEY = os.getenv('SANIC_SECRET', 'Secret')
    RESONSE_TIMEOUT = 600
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
