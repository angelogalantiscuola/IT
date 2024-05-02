# tests/test_routes.py
def test_get_books(client):
    # The client in your test functions is a fixture provided by the pytest-flask plugin.
    # It represents a test client that you can use to make requests to your Flask application
    # without needing to run an actual server.
    # The client fixture is typically defined in your conftest.py file
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_book(client):
    # Test with existing book ID
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["title"] == "Book 1"

    # Test with non-existing book ID
    response = client.get("/books/100")
    assert response.status_code == 404
    assert response.json["error"] == "Book not found"
