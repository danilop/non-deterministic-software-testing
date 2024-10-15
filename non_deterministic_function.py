import random

def non_deterministic_function(x):
    if random.random() < 0.1:  # 10% chance of failure
        return None
    return x * 2

# Running this function multiple times with the same input
for _ in range(20):
    result = non_deterministic_function(5)
    print(result)
