const baseUrl = 'http://127.0.0.1:5000';

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

document.getElementById('getUsers').addEventListener('click', () => {
  fetch(`${baseUrl}/users`)
    .then(response => response.json())
    .then(users => {
      const usersList = document.getElementById('usersList');
      usersList.innerHTML = '';
      users.forEach(user => {
        const userItem = document.createElement('div');
        userItem.textContent = `ID: ${user.id}, Name: ${user.name}`;
        usersList.appendChild(userItem);
      });
    });
});

document.getElementById('addUser').addEventListener('click', () => {
  const userName = document.getElementById('userName').value;
  const newUser = { name: userName };

  fetch(`${baseUrl}/users`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newUser)
  })
    .then(response => response.json())
    .then(user => {
      console.log(user);
      document.getElementById('userName').value = '';
    });
});
