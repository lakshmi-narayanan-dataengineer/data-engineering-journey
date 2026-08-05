"""
Pandas Basics: DataFrame Creation & Exploration
-----------------------------------------------
Pandas is an essential library for data analysis and manipulation.
This script demonstrates basic DataFrame creation and basic inspection methods.
"""

import pandas as pd


# 1. Define dataset as a Python dictionary
data = {
    "Name": ["Alice", "Bob", "John"],
    "Age": [24, 25, 26]
}

# 2. Convert dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# 3. Basic Visual Display
print("--- DataFrame Output ---")
print(df)

# 4. Quick Inspection Methods (Essential for Data Engineering)
print("\n--- DataFrame Summary Info ---")
print(df.info())

print("\n--- DataFrame Summary Statistics ---")
print(df.describe())