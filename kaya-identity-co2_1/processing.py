import pandas as pd


df = pd.read_csv("kaya-identity-co2.csv", quotechar='"') # , on_bad_lines="skip"
print(df.columns)


am_I_reading = False 
# 





# Checks if you are able to read your csv file
if am_I_reading: 
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



# # Load the dataset
# df = pd.read_csv("kaya-identity-co2.csv")

# # Print column names to verify what it's called
# print("Available columns:", df.columns.tolist())

# # Sort the dataframe by the annual emission column (adjust name as needed)
# # Example: "Annual CO2 Emissions" or "CO2_Emissions" or similar
# sorted_df = df.sort_values(by="Annual CO2 Emissions", ascending=False)

# # Display the top rows
# print("\nTop countries/years by CO2 emissions:")
# print(sorted_df.head())

# # Save to new CSV
# sorted_df.to_csv("sorted_emissions.csv", index=False)
