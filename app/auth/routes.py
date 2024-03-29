from flask import redirect, request, flash, render_template, url_for
from flask_login import login_user, current_user, login_required, logout_user

from app import db, bcrypt
from app.auth import auth_bp
from app.models.forms import RegisterForm, LoginForm
from app.models.auth import User


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return 'url main page'
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("You registered and are now logged in. Welcome!", "success")

        return redirect('/')

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("auth/login.html", form=form)
    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("auth.login"))