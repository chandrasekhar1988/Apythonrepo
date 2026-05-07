#General Addition
def add(x, y):
    return x + y

#దీన్నే లాంబ్డాలో ఇలా రాస్తాం:
lambda_add = lambda x, y : x + y

result1 = add(5, 3)
print(f"Normal Function Result: {result1}")

# Calling the lambda function
result2 = lambda_add(7, 8)
print(f"Lambda Function Result: {result2}")