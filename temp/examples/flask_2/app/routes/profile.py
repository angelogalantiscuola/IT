from flask import Blueprint, render_template, request, flash, session
from ..models.user import User
from ..auth import login_required

profile = Blueprint("profile", __name__)


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def view():
    user = User.get_by_id(session["user_id"])

    if request.method == "POST":
        username = request.form["username"]
        # Update username
        user.username = username
        user.save()
        session["username"] = username
        flash("Profile updated")

    return render_template("profile.html", user=user)
