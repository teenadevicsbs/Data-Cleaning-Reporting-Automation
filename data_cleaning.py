import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("student_data.xlsx")

print("Original Data:")
print(df)

# Handle missing values
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

df["City"] = df["City"].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_excel("cleaned_sales_data.xlsx", index=False)

# Create report
report = pd.DataFrame({
    "Metric": ["Total Records", "Average Sales"],
    "Value": [len(df), round(df["Sales"].mean(), 2)]
})

report.to_excel("sales_report.xlsx", index=False)

# Create chart
sales_summary = df.groupby("Product")["Sales"].sum()

sales_summary.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")

print("\nProject Completed Successfully!")
print("Generated Files:")
print("- cleaned_sales_data.xlsx")
print("- sales_report.xlsx")
print("- sales_chart.png")