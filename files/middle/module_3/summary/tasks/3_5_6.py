
# Define a global counter
call_count = 0

def call_counter():
    global call_count
    call_count += 1
    return call_count

# Demonstrate the function
print("Counter before any calls:", call_count)
print("Counter after 1st call:", call_counter())
print("Counter after 2nd call:", call_counter())
print("Counter after 3rd call:", call_counter())
