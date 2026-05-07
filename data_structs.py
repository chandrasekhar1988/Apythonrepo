# 1. List (సర్వర్ల జాబితా) - ఇది మారుస్తూ ఉండవచ్చు
servers = ["web-01", "db-01", "app-01"]
print("List (సర్వర్లు):", servers)
print(servers[0])  # మొదటిది (web-01) ప్రింట్ అవుతుంది
servers.append("cache-01") # కొత్త సర్వర్‌ని యాడ్ చేయడం

# 2. Tuple (మారకూడని కాన్ఫిగరేషన్) - ఇది ఒకసారి పెడితే అంతే
config_data = ("us-east-1", "t2.micro")
print("Tuple (AWS కాన్ఫిగరేషన్):", config_data)
print(config_data[1]) # మనం మార్చలేము, కానీ చదవగలం


# 3. Dictionary (Key-Value తో సర్వర్ వివరాలు)
server_details = {"name": "prod-server", "ip": "10.0.0.5", "status": "active"}
print("Dictionary (సర్వర్ వివరాలు):", server_details)

# 4. Set (యూనిక్ పోర్ట్స్) - డూప్లికేట్స్ ఉండవు
#మీకు డూప్లికేట్ డేటా వద్దు అనుకున్నప్పుడు మరియు 
# డేటా ఏ క్రమంలో ఉన్నా పర్వాలేదు అనుకున్నప్పుడు 'Set' వాడాలి.
ports = {80, 443, 80, 22} # 80 రెండుసార్లు ఉన్నా, అది ఒక్కసారే చూపిస్తుంది
print("Set (ఓపెన్ పోర్ట్స్ - డూప్లికేట్స్ తీసేస్తుంది):", ports)