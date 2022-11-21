import roblox


client = roblox.Client()

@client.event
def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
def on_follower(user):
    print(f"{user.name} followed client user")

client.run(
    cookie="cookie_here"
)

