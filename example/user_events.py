import roblox


client = roblox.Client()

@client.event
def on_ready():
    # This is ran when the client has started all the events, code etc.
    print(f"Logged in as {client.user.name}")

@client.event
def on_follower(user):
    # When a user follows the client it will pass the User object of the person who followed
    print(f"{user.name} followed client user")

# Logins to the cookie will return an error if the cookie is invalid
client.run(
    cookie="cookie_here"
)
