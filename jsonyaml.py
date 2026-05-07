import json

# పైథాన్ డిక్షనరీని JSON స్ట్రింగ్‌గా మార్చడం (Serialization)
data = {"name": "Chandra", "role": "DevOps"}
json_string = json.dumps(data) 
print(json_string) # రిజల్ట్: {"name": "Chandra", "role": "DevOps"}