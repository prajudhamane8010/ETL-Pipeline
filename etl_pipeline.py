import pandas as pd

print("=" * 50)
print("        ETL PIPELINE PROJECT")
print("=" * 50)

# Step 1: Extract
print("\nStep 1: Reading Dataset...")
df = pd.read_csv("dataset/superstore_sales.csv")

print("Dataset Loaded Successfully!")

print("\nFirst 5 Rows:")
print(df.head())

# Step 2: Transform
print("\nStep 2: Cleaning Dataset...")

duplicates = df.duplicated().sum()
print(f"Duplicate Rows: {duplicates}")

df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())

if "Sales" in df.columns and "Quantity" in df.columns:
    df["Sales_per_Item"] = df["Sales"] / df["Quantity"]
    print("\nNew Column Added: Sales_per_Item")

# Step 3: Load
print("\nStep 3: Saving Cleaned Dataset...")

df.to_csv("cleaned_superstore_sales.csv", index=False)

print("Cleaned Dataset Saved Successfully!")

print("\n" + "=" * 50)
print("ETL PIPELINE COMPLETED SUCCESSFULLY!")
print("=" * 50)