# వేరియబుల్స్ నిర్వచనం
x = 100
y = 10.5
z = "Hello"

# టేబుల్ హెడర్ (Table Header)
print("-" * 40)
print(f"{'Variable':<12} | {'Value':<12} | {'Data Type':<10}")
print("-" * 40)

# f-strings ఉపయోగించి అమరిక
print(f"{'x':<12} | {x:<12} | {type(x).__name__}")
print(f"{'y':<12} | {y:<12} | {type(y).__name__}")
print(f"{'z':<12} | {z:<12} | {type(z).__name__}")

print("-" * 40)


