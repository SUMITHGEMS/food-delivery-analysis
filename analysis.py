import pandas as pd

# Load dataset
df = pd.read_csv("food_delivery.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert to numeric
df['delivery_person_age'] = pd.to_numeric(df['delivery_person_age'], errors='coerce')
df['delivery_person_ratings'] = pd.to_numeric(df['delivery_person_ratings'], errors='coerce')

# ✅ FIXED WAY (NO inplace=True)

df['delivery_person_age'] = df['delivery_person_age'].fillna(df['delivery_person_age'].mean())

df['delivery_person_ratings'] = df['delivery_person_ratings'].fillna(df['delivery_person_ratings'].mean())

df['weather_conditions'] = df['weather_conditions'].fillna(df['weather_conditions'].mode()[0])

df['road_traffic_density'] = df['road_traffic_density'].fillna(df['road_traffic_density'].mode()[0])

df['city'] = df['city'].fillna(df['city'].mode()[0])

df['festival'] = df['festival'].fillna("No")

df['multiple_deliveries'] = df['multiple_deliveries'].fillna(0)

# Drop missing important column
df = df.dropna(subset=['time_orderd'])

# Remove duplicates
df = df.drop_duplicates()

# Final check
print("CLEANED DATA:")
print(df.isnull().sum())

# Save
df.to_csv("cleaned_food_delivery.csv", index=False)

print("\n--- ANALYSIS START ---")

# 1. Average delivery time
print("\nAverage Delivery Time:")
print(df['time_taken_(min)'].mean())

# 2. Delivery time by city
print("\nDelivery Time by City:")
print(df.groupby('city')['time_taken_(min)'].mean().sort_values())

# 3. Delivery time by traffic
print("\nDelivery Time by Traffic:")
print(df.groupby('road_traffic_density')['time_taken_(min)'].mean().sort_values())

# 4. Delivery time by vehicle
print("\nDelivery Time by Vehicle:")
print(df.groupby('type_of_vehicle')['time_taken_(min)'].mean().sort_values())

# 5. Orders per city
print("\nOrders per City:")
print(df['city'].value_counts())

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Delivery Time by City
plt.figure()
sns.barplot(x='city', y='time_taken_(min)', data=df)
plt.title("Delivery Time by City")
plt.show()

# 2. Delivery Time by Traffic
plt.figure()
sns.barplot(x='road_traffic_density', y='time_taken_(min)', data=df)
plt.title("Delivery Time by Traffic")
plt.show()

# 3. Delivery Time by Vehicle
plt.figure()
sns.barplot(x='type_of_vehicle', y='time_taken_(min)', data=df)
plt.title("Delivery Time by Vehicle")
plt.show()
