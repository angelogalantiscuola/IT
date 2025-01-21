from flask import render_template, request, redirect, url_for, jsonify
from . import entries
from ..models.entry import Entry
from ..auth import login_required


@entries.route("/")
def list():
    search = request.args.get("search")
    entries_list = Entry.get_all(search)
    return render_template("list.html", entries=entries_list)


@entries.route("/entries/new", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        entry = Entry(name=name, message=message)
        entry.save()
        return redirect(url_for("entries.list"))
    return render_template("create.html")


@entries.route("/entries/<int:id>", methods=["GET"])
def read(id):
    entry = Entry.get_by_id(id)
    if entry:
        return render_template("read.html", entry=entry)
    return jsonify({"message": "Entry not found"}), 404


@entries.route("/entries/<int:id>/edit", methods=["GET", "POST"])
@login_required
def update(id):
    entry = Entry.get_by_id(id)
    if not entry:
        return jsonify({"message": "Entry not found"}), 404

    if request.method == "POST":
        entry.name = request.form["name"]
        entry.message = request.form["message"]
        entry.save()
        return redirect(url_for("entries.list"))
    return render_template("update.html", entry=entry)


@entries.route("/entries/<int:id>/delete", methods=["GET", "POST"])
@login_required
def delete(id):
    entry = Entry.get_by_id(id)
    if not entry:
        return jsonify({"message": "Entry not found"}), 404

    if request.method == "POST":
        entry.delete()
        return redirect(url_for("entries.list"))
    return render_template("delete.html", entry=entry)
