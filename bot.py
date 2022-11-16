import roblox


client = roblox.Client()

@client.event
def on_ready():
    print(f"Client started")
    #print(client.user.id)

client.run(
    cookie="cookie here"
)

