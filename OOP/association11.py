class User:
    def __init__(self, username):
        self.username = username
        self.profile = Profile(self) # Reference to Profile object

class Profile:
    def __init__(self, user):
        self.bio = ""
        self.user = user # Reference to User object
        # The back-reference to User can be useful in scenarios 
        # where you have a Profile instance and need to access 
        # the associated User's data.

# Example of usage
user1 = User("Alice")
user1.profile.bio = "Hello, I'm Alice!"

user2 = User("Bob")
user2.profile.bio = "Hello, I'm Bob!"

print(user1.username, user1.profile.bio)
print(user2.username, user2.profile.bio)
