from flask import render_template, request, flash
from . import profile
from ..models.user import User
from ..auth import login_required


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def view():
    from flask import session

    user = User.get_by_id(session["user_id"])

    if request.method == "POST":
        username = request.form["username"]
        # Update username
        user.username = username
        user.save()
        session["username"] = username
        flash("Profile updated")

    return render_template("profile.html", user=user)
