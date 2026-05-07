#సాధారణ పద్ధతి (For Loop):ఇక్కడ మనం 3-4 లైన్ల కోడ్ రాయాలి.
all_servers = ["prod-web", "test-db", "prod-api", "dev-cache"]
prod_only = []

for s in all_servers:
    if "prod" in s:
        prod_only.append(s)


# List Comprehension అదే పనిని ఒక్క లైన్‌లో ఇలా చేయవచ్చు:

all_servers = ["prod-web", "test-db", "prod-api", "dev-cache"]
prod_only = [s for s in all_servers if "prod" in s]
print(prod_only) # Output: ['prod-web', 'prod-api']


# DevOps లో కొన్నిసార్లు మనం పేర్లను ఒకే ఫార్మాట్లోకి Capital Letters మార్చాల్సి ఉంటుంది
servers = ["web", "db", "app"]

# అన్నీ Uppercase లోకి మార్చు
upper_servers = [s.upper() for s in servers]

print(upper_servers) # Output: ['WEB', 'DB', 'APP']