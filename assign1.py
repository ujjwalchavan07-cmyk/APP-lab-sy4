import pandas as pd
import numpy as np

np.random.seed(42)
s = pd.Series(np.random.randint(1, 100, 10))

print("Original Series:")
print(s)

print("\nFirst element:", s[0])
print("Element at index 4:", s[4])
print("First five elements:\n", s[:5])

print("\nNumbers greater than 50:")
print(s[s > 50])

print("\nEven numbers:")
print(s[s % 2 == 0])

print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

print("\nStatistical Summary:")
print(s.describe())