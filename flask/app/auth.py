from functools import wraps
from flask import session, redirect, url_for
from .models.user import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        return None
    return User.get_by_id(user_id)
