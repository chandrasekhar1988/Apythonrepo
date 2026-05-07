# For Loop (సర్వర్ల లిస్ట్ కోసం)
servers = ["web", "db", "cache"]
for s in servers:
    print("చెక్ చేస్తున్నాను:", s)

# While Loop (సర్వర్ అప్ అయ్యే వరకు వెయిట్ చేయడం)
retry = 0
while retry < 3:
    print("సర్వర్ కనెక్ట్ అవ్వడానికి ట్రై చేస్తున్నాను...")
    retry += 1