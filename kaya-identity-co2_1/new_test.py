import pandas as pd
import matplotlib.pyplot as plt
import os

# === 1. Load and clean data ===
print("🔄 Loading data...")
df = pd.read_csv("kaya-identity-co2.csv", quotechar='"')
df.columns = df.columns.str.strip()
df["Entity"] = df["Entity"].str.strip()

# === 2. Filter by year ===
df = df[(df["Year"] >= 1990) & (df["Year"] <= 2023)]

# === 3. Choose which entities to include ===
target_entities = [
    "United States",
    "China",
    "India",
    "Germany",
    "Brazil",
    "Japan"
]

filtered_df = df[df["Entity"].isin(target_entities)]
plot_columns = [col for col in filtered_df.columns if col not in ["Entity", "Code", "Year"]]

# === 4. Prepare output folder ===
output_dir = "entity_plots"
os.makedirs(output_dir, exist_ok=True)

# === 5. Generate plots ===
print(f"📊 Generating plots for {len(target_entities)} entities...")

plot_count = 0
for entity, group in filtered_df.groupby("Entity"):
    group = group.sort_values("Year")
    
    for col in plot_columns:
        data = group[["Year", col]].dropna()
        if data.empty:
            continue

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(data["Year"], data[col], marker='o', linestyle='-')
        plt.title(f"{entity} — {col}")
        plt.xlabel("Year")
        plt.ylabel(col)
        plt.grid(True)
        plt.tight_layout()

        # Save
        safe_entity = entity.replace(" ", "_").replace("/", "-")
        safe_col = col.replace(" ", "_").replace("/", "-")
        filename = f"{safe_entity}__{safe_col}.png"
        plt.savefig(os.path.join(output_dir, filename))
        plt.close()
        plot_count += 1

print(f"\n✅ Done! {plot_count} plots saved to: '{output_dir}/'")
