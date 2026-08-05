import pandas as pd
import json

# JSON String representation
json_data = '{"name": "Anu", "Age": 23, "dept": "CSE"}'

# Read JSON string into DataFrame (using pd.read_json)
df = pd.read_json(json_data, typ="series")
print(df)