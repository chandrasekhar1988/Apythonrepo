status = 200 # HTTP కోడ్
if status == 200:
    print("సర్వర్ బాగుంది (OK)")
elif status == 404:
    print("సర్వర్ దొరకలేదు (Not Found)")
else:
    print("ఏదో తేడాగా ఉంది!")