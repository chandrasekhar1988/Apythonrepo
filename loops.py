# For Loop (సర్వర్ల లిస్ట్ కోసం)
servers = ["web", "db", "cache"]
for s in servers:
    print("Checking server:", s)

# While Loop (సర్వర్ అప్ అయ్యే వరకు వెయిట్ చేయడం)
retry = 0
while retry < 3:
    print("Attempting to connect to server...")
    retry += 1