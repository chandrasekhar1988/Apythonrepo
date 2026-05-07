# 1. Module ని ఇంపోర్ట్ చేయడం (టూల్ బాక్స్)
from functools import reduce
#Module (from functools import reduce): పైథాన్‌లో reduce అనేది నేరుగా రాదు, 
#అది functools అనే మాడ్యూల్ (పెట్టె) లో ఉంటుంది. అందుకే దాన్ని ముందుగా import చేసుకున్నాం.

# ఉదాహరణకు AWS నుండి వచ్చిన డేటా అనుకుందాం
instance_ids = ["i-123", "i-456", "i-789"]
instance_costs = [10.5, 25.0, 15.25]  # ఒక్కో సర్వర్ ఖర్చు (Dollars)

print("--- DevOps Automation Report ---")

# 2. Map వాడకం: అన్ని సర్వర్ ఐడిలకు 'prod-' అని పేరు మార్చడం
# (Bulk Operation: Transforming every item in the list)
prod_instances = list(map(lambda id: "prod-" + id, instance_ids))
print(f"Production Instance Names: {prod_instances}")

# 3. Reduce వాడకం: మొత్తం సర్వర్ల ఖర్చును లెక్కించడం
# (Aggregating: Combining all items into one single value)
total_bill = reduce(lambda x, y: x + y, instance_costs)

print(f"Monthly Total Bill: ${total_bill}")
print("--------------------------------")