import json
import yaml
# 1. JSON ఫైల్ చదవడం
data = {
    "project": "DevOps-Automation",
    "version": 1.0,
    "tools": ["Jenkins", "Docker", "Python"]
}

# JSON కి సేవ్ చేయడం
with open("config.json", "w") as f:
    json.dump(data, f, indent=4)
print("JSON file has been created.")


# 2. YAML ఫైల్ చదవడం (Real-time లో Kubernetes/Ansible కి ఇది చాలా ముఖ్యం)
yaml_data = """
server:
  app_name: MyWebApp
  port: 80
  environment: production
"""
parsed_yaml = yaml.safe_load(yaml_data)
print(f"YAML లోని App Name: {parsed_yaml['server']['app_name']}")



