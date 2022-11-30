import roblox

client = roblox.Client()
for i in range(2000):
    try:
        user = client.fetch_user(i+1)
        print(user.name)
        
    except roblox.models.ErrorModel.InvalidUser:
        print(f"{i+1} ID is not found")
        
    except roblox.models.ErrorModel.RateLimit:
        print(f"Ratelimited")
