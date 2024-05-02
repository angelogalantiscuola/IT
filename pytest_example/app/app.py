from flask import Flask, jsonify, render_template

app = Flask(__name__)

books = [{"id": 1, "title": "Book 1"}, {"id": 2, "title": "Book 2"}, {"id": 3, "title": "Book 3"}]


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    #  using a generator expression instead of a list comprehension can be more efficient
    # in terms of memory usage and performance.
    # It doesn't create a new list in memory, so it can be more memory-efficient, especially for large lists.
    # With a generator expression, this means that Python stops generating items as soon as it finds a match.
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route("/list-books")
def list_books():
    return render_template("books.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)
