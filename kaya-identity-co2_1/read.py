
# Checks if you are able to read your csv file

import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv("kaya-identity-co2.csv", quotechar='"') # , on_bad_lines="skip"
print(df.columns)

  

# 🔍 Print column names and number of columns
print("Column names:", df.columns.tolist())
print("Number of columns:", len(df.columns))

# ✅ Check that every row has the same number of columns
# This finds any rows with missing or extra columns (NaNs mean missing values)
row_lengths = df.apply(lambda row: row.count(), axis=1)  # counts non-NaN fields per row
print("\nSummary of non-null fields per row:")
print(row_lengths.value_counts().sort_index())

# Optional: flag any rows with fewer or more non-null fields
expected_columns = len(df.columns)
bad_rows = df[row_lengths != expected_columns]
print(f"\nNumber of rows with incomplete data: {len(bad_rows)}")

print(f"\nTotal rows: {len(df)}")

