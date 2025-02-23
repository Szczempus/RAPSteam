
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x += 5
    
    inner()
    return x

# Example usage
result = outer()
print(result)  # Output should be 15
