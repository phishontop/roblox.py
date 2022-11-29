import roblox

client = roblox.Client()
user = client.fetch_user(1)
print(user.name)

user = client.fetch_user(3)
print(user.description)