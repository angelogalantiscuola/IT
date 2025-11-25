from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if User.get_by_username(username):
            flash("Username already exists")
            return redirect(url_for("auth.register"))

        user = User(username=username, password=password)
        user.save()
        return redirect(url_for("auth.login"))
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.get_by_username(username)
        if user and user.verify_password(password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("entries.list"))
        flash("Invalid username or password")
    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


@auth.route("/password_reset_request", methods=["GET", "POST"])
def password_reset_request():
    if request.method == "POST":
        _ = request.form["email"]
        # Logic to send password reset email goes here
        flash("Password reset email sent")
        return redirect(url_for("auth.login"))
    return render_template("password_reset_request.html")


@auth.route("/password_reset/<token>", methods=["GET", "POST"])
def password_reset(token):
    if request.method == "POST":
        _ = request.form["password"]
        # Logic to reset the password goes here
        flash("Password has been reset")
        return redirect(url_for("auth.login"))
    return render_template("password_reset.html", token=token)
