import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Simulated historical test data
# Features: input_a, input_b, system_load
# Target: 0 (pass) or 1 (fail)
X = np.array([
    [1, 2, 0.5], [2, 3, 0.7], [3, 4, 0.3], [4, 5, 0.8], [5, 6, 0.4],
    [2, 2, 0.6], [3, 3, 0.5], [4, 4, 0.7], [5, 5, 0.2], [6, 6, 0.9]
])
y = np.array([0, 0, 0, 1, 0, 0, 0, 1, 0, 1])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Function to generate new test cases
def generate_test_cases_from_historical_test_data(n_cases):
    # Generate random inputs
    new_cases = np.random.rand(n_cases, 3)
    new_cases[:, 0] *= 10  # Scale input_a to 0-10
    new_cases[:, 1] *= 10  # Scale input_b to 0-10
    
    # Predict failure probability
    failure_prob = clf.predict_proba(new_cases)[:, 1]
    
    # Sort cases by failure probability
    sorted_indices = np.argsort(failure_prob)[::-1]
    
    return new_cases[sorted_indices]

# Generate and print top 5 test cases most likely to fail
top_test_cases = generate_test_cases_from_historical_test_data(100)[:5]
print("Top 5 test cases most likely to fail:")
for i, case in enumerate(top_test_cases, 1):
    print(f"Case {i}: input_a = {case[0]:.2f}, input_b = {case[1]:.2f}, system_load = {case[2]:.2f}")
