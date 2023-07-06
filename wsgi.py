import logging
from app import create_app
from app.extensions import login_manager
from app.models.auth import User

logging.basicConfig(level=logging.DEBUG)
app = create_app()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


#serve(app, host=c.HOST, port=c.PORT)
app.run(port=5022)