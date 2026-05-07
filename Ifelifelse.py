status = 200 # HTTP కోడ్
if status == 200:
    print("serverisok (OK)")
elif status == 404:
    print("No server (Not Found)")
else:
    print("something fishy!")