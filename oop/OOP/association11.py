class User:
    def __init__(self, username: str):
        self.username = username
        self.profile = Profile() # Reference to Profile object

class Profile:
    def __init__(self):
        self.bio = ""

# Example of usage
user1 = User("Alice")
user1.profile.bio = "Hello, I'm Alice!"

user2 = User("Bob")
user2.profile.bio = "Hello, I'm Bob!"

print(user1.username, user1.profile.bio)
print(user2.username, user2.profile.bio)

