import numpy as np
from scipy import stats

class AnomalyDetector:
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.values = []

    def add_value(self, value):
        self.values.append(value)
        if len(self.values) > self.window_size:
            self.values.pop(0)

    def is_anomaly(self, new_value, z_threshold=3.0):
        if len(self.values) < self.window_size:
            return False  # Not enough data to detect anomalies yet
        
        mean = np.mean(self.values)
        std = np.std(self.values)
        
        if std == 0:
            return False # To avoid an error if all values are the same.
        
        z_score = (new_value - mean) / std
        
        return abs(z_score) > z_threshold

# Usage
detector = AnomalyDetector()

# Simulate some normal values
for _ in range(100):
    detector.add_value(np.random.normal(0, 1))

# Test with a normal value
print(detector.is_anomaly(1.5))  # Probably False

# Test with an anomaly
print(detector.is_anomaly(10))  # Probably True
