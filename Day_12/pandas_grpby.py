"""
Pandas Data Merging & Relational Joins

Demonstrates SQL-style joins (Inner, Left, Right, Outer) using `pd.merge()`.
This mimics relational database joins common in Data Engineering pipelines.
"""

import pandas as pd
# 1. Datasets Creation (Simulating Relational Database Tables)


# Primary Table: Customers (Includes customer 5, who has no orders)
customers_df = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'country': ['US', 'UK', 'CA', 'US', 'IN']
})

# Transactional Table: Orders (Includes order 105, which has an unmapped customer_id 99)
orders_df = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'c_id': [1, 2, 2, 4, 99],  # Note: 'c_id' maps to 'customer_id'
    'amount_usd': [250.00, 450.50, 120.00, 89.99, 300.00]
})

print("--- Customers Table ---")
print(customers_df)
print("\n--- Orders Table ---")
print(orders_df)

# 2. Inner Join (Matches only where keys exist in BOTH tables)

# Note: left_on and right_on are used when column names differ across tables.

inner_merged = pd.merge(
    customers_df, 
    orders_df, 
    left_on='customer_id', 
    right_on='c_id', 
    how='inner'
)

print("\n=== INNER JOIN ===")
print("(Only customers with active orders)")
print(inner_merged[['customer_id', 'customer_name', 'order_id', 'amount_usd']])


# 3. Left Join (Keeps ALL customers, fills missing order details with NaN)


left_merged = pd.merge(
    customers_df, 
    orders_df, 
    left_on='customer_id', 
    right_on='c_id', 
    how='left'
)

print("\n=== LEFT JOIN ===")
print("(All customers included; Eve will have NaN order details)")
print(left_merged[['customer_id', 'customer_name', 'order_id', 'amount_usd']])


# 4. Outer Join (Keeps ALL records from both tables)


outer_merged = pd.merge(
    customers_df, 
    orders_df, 
    left_on='customer_id', 
    right_on='c_id', 
    how='outer'
)

print("\n=== FULL OUTER JOIN ===")
print("(Includes unmatched customers AND orphaned orders)")
print(outer_merged[['customer_id', 'customer_name', 'order_id', 'amount_usd']])