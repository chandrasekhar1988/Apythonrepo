# Server memory limit example
memory_usage = 7

# 1. Using 'in' operator to check if status is valid
allowed_statuses = ["active", "idle", "restarting"]
current_status = "active"

if current_status in allowed_statuses:
    print("Status is valid.")

# 2. Chained Comparison Operator (Checking range)
# Instead of: if memory_usage > 5 and memory_usage < 10:
if 5 < memory_usage < 10:
    print("Memory usage is within the safe limit (between 5 and 10).")

# 3. Logical Operators (and, or, not)
is_admin = True
has_permission = False

if is_admin and has_permission:
    print("Access granted.")
elif is_admin or has_permission:
    print("Limited access.")
else:
    print("Access denied.")

# Server status check
current_status = "error"
expected_status = "ok"

# Using '==' to check if they are equal
if current_status == expected_status:
    print("Everything is working fine.")

# Using '!=' to check if they are NOT equal
if current_status != expected_status:
    print("Warning: Server is not in the expected state!")