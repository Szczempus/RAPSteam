
def weighted_average(values, weights):
    if len(values) != len(weights):
        raise ValueError("Lists must have the same length")
    
    total_weight = sum(weights)
    weighted_sum = sum(value * weight for value, weight in zip(values, weights))
    
    return weighted_sum / total_weight


values = [10, 20, 30]
weights = [1, 2, 3]
print(f"Wartości: {values}")
print(f"Wagi: {weights}")
print(weighted_average(values, weights))  

