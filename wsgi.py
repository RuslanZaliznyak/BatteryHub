import logging

from waitress import serve

from app import create_app

from app.config import Config as c

logging.basicConfig(level=logging.DEBUG)
app = create_app()
serve(app, host=c.HOST, port=c.PORT)
