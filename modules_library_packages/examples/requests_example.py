import requests

# Making a GET request
response = requests.get("https://api.github.com")
# response = requests.get("https://github.com")
# response = requests.get("https://github.com/sdadsaddafafdsd")

# Checking the status code of the request
print(response.status_code)

# Printing the content of the response
print(type(response.text))
data = response.json()
print(data)
print(type(data))
print(data["current_user_url"])
