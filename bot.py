import roblox


client = roblox.Client()

@client.event
def on_ready():
    print(f"Logged in as {client.user.name}")

client.run(
    cookie="cookie_here"
)

