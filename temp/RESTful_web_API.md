# RESTful web API with JS as client and python as web server

## Server-side code (Python)

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        # Retrieve data from a database or other source
        users = [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Jane Doe"},
        ]
        return jsonify(users)

    def post(self):
        # Create a new user
        new_user = request.get_json()
        users.append(new_user)
        return jsonify(new_user)

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)
```

## Client-side code (JavaScript)

```javascript
const fetch = require('node-fetch');

const baseUrl = 'http://localhost:5000';

fetch(`${baseUrl}/users`)
  .then(response => response.json())
  .then(users => console.log(users));

const newUser = {
  name: 'Peter Jones'
};

fetch(`${baseUrl}/users`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(newUser)
})
  .then(response => response.json())
  .then(user => console.log(user));
```
