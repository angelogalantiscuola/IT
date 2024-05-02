# tests/test_templates.py
def test_list_books(client):
    response = client.get("/books")
    assert response.status_code == 200

    # Render the template with the app context
    html = response.get_data(as_text=True)

    # Assert that the rendered template contains the expected content
    assert "<h1>Books</h1>" in html
    assert "<li>Book 1</li>" in html
    assert "<li>Book 2</li>" in html
    assert "<li>Book 3</li>" in html
