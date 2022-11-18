import roblox


client = roblox.Client()

@client.event
def on_ready():
    print(f"Logged in as {client.user.name}")
    print(f"Client User has {client.user.get_friend_count()} friends")

@client.event
def on_follower():
    print(f"{client.user.name} got a new follower")

client.run(
    cookie=""
)

