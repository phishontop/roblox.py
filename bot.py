import roblox
import threading

client = roblox.Client()

user = client.fetch_user(1)
print(user.name)
group = client.fetch_group(1)
print(group.name)
