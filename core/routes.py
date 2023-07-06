from flask import render_template
from flask_login import login_required
from app.core import core_bp


@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")