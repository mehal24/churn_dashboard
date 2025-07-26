import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv(r"C:\Users\mehal\OneDrive\Desktop\SEM-3\DATA ANALYTICS\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Preview
print(df.head())
print(df.info())

# Clean TotalCharges (convert to numeric)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
df.dropna(subset=["TotalCharges"], inplace=True)

# Convert Churn to binary
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Basic Churn Stats
print("Churn Rate:", df["Churn"].mean())

# Plot churn by contract type
plt.figure(figsize=(6, 4))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Churn by Contract Type")
plt.show()

# Plot churn by tenure buckets
df['TenureGroup'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72], labels=["0-12", "13-24", "25-48", "49-72"])
plt.figure(figsize=(6, 4))
sns.countplot(x='TenureGroup', hue='Churn', data=df)
plt.title("Churn by Tenure")
plt.show()


# Set visual style
sns.set(style="whitegrid")

# Churn vs Internet Service
plt.figure(figsize=(6, 4))
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.title("Churn by Internet Service Type")
plt.show()

# Churn vs Payment Method
plt.figure(figsize=(8, 4))
sns.countplot(x='PaymentMethod', hue='Churn', data=df)
plt.title("Churn by Payment Method")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Charges Distribution by Churn
plt.figure(figsize=(6, 4))
sns.kdeplot(data=df[df['Churn'] == 0], x='MonthlyCharges', label='Not Churned')
sns.kdeplot(data=df[df['Churn'] == 1], x='MonthlyCharges', label='Churned')
plt.title("Monthly Charges Distribution by Churn")
plt.legend()
plt.show()

# Total Charges Distribution by Churn
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='TotalCharges', hue='Churn', bins=10, kde=True)
plt.title("Total Charges vs Churn")
plt.show()
