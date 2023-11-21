// Description: This file contains the code to test the API endpoints

// Import the node-fetch package
const fetch = require('node-fetch');

// Define the base URL
const baseUrl = 'http://localhost:5000';

// Test the GET /users endpoint
fetch(`${baseUrl}/users`)
    .then(response => response.json()) // Convert the response to JSON
    .then(users => console.log(users)); // Print the JSON data

const newUser = {
    name: 'Peter Jones'
};

// Test the POST /users endpoint
fetch(`${baseUrl}/users`, {
    method: 'POST', // Set the HTTP method as POST
    headers: {
        'Content-Type': 'application/json' // Tell the server we are sending JSON data
    },
    body: JSON.stringify(newUser) // Convert the JavaScript object to JSON
})
    .then(response => response.json()) // Convert the response to JSON
    .then(user => console.log(user)); // Print the JSON data
