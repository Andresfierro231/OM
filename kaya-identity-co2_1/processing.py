import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv("kaya-identity-co2.csv", quotechar='"') # , on_bad_lines="skip"
print(df.columns)



# Load CSV with appropriate quoting
df = pd.read_csv("kaya-identity-co2.csv", quotechar='"')

# Strip any leading/trailing whitespace from column names
df.columns = df.columns.str.strip()

# Filter by year
df = df[(df["Year"] >= 1990) & (df["Year"] <= 2023)]

# Create output folder for plots
output_dir = "entity_plots"
os.makedirs(output_dir, exist_ok=True)

# List of columns to plot (exclude Entity, Code, Year)
plot_columns = [col for col in df.columns if col not in ["Entity", "Code", "Year"]]

# Group by Entity
for entity, group in df.groupby("Entity"):
    # Sort by Year just in case
    group = group.sort_values("Year")
    
    # Generate one plot per variable
    for col in plot_columns:
        # Skip if the column is entirely NaN
        if group[col].dropna().empty:
            continue
        
        plt.figure(figsize=(10, 6))
        plt.plot(group["Year"], group[col], marker='o', linestyle='-', label=col)
        plt.title(f"{entity}: {col}")
        plt.xlabel("Year")
        plt.ylabel(col)
        plt.grid(True)
        plt.tight_layout()
        
        # Sanitize filename
        safe_entity = entity.replace(" ", "_").replace("/", "-")
        safe_col = col.replace(" ", "_").replace("/", "-")
        filename = f"{safe_entity}__{safe_col}.png"
        filepath = os.path.join(output_dir, filename)
        
        plt.savefig(filepath)
        plt.close()

print(f"✅ Plots saved to: {output_dir}")


# Column names: 
# ['Entity', 
# 'Code', 
# 'Year', 
# 'Annual CO₂ emissions', 
# 'Primary energy consumption per GDP (kWh/$)', 
# 'GDP per capita', 
# '900793-annotations', 
# 'Population (historical)', 
# 'Annual CO₂ emissions per unit energy (kg per kilowatt-hour)', 
# 'Annual CO₂ emissions per GDP (kg per international-$)']

# Number of columns: 10

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
