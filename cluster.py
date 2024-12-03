import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from dataset import collect_data  # Import the function to collect data

# Step 1: Create a fictitious dataset
data = collect_data()  # Collect data provided by the user
df = pd.DataFrame(data)  # Convert the collected data into a pandas DataFrame

# Display the keys (column names) available in the dataset
print("-" * 32)
print("\nThese are the keys available in the dataset:\n")
print(list(data.keys()))  # Show the available keys for reference

# Function to take user input for selecting the columns
def get_user_input():
    """
    Prompts the user to input column names for:
    - `key1`: Label column (e.g., city names)
    - `key2`: First numeric column for clustering (e.g., tomatoes sales)
    - `key3`: Second numeric column for clustering (e.g., bread sales)
    """
    key1 = input("Enter the first key of the dictionary (e.g., labels or city names): ")
    key2 = input("Enter the second key of the dictionary (numeric values for clustering): ")
    key3 = input("Enter the third key of the dictionary (numeric values for clustering): ")
    return key1, key2, key3

# Get the keys from the user
key1, key2, key3 = get_user_input()

# Validate the keys entered by the user
if key1 not in df.columns or key2 not in df.columns or key3 not in df.columns:
    raise ValueError("One or more keys do not exist in the dataset. Please check your input.")

# Ensure the columns selected for clustering are numeric
if not np.issubdtype(df[key2].dtype, np.number) or not np.issubdtype(df[key3].dtype, np.number):
    raise ValueError(f"The columns '{key2}' and '{key3}' must be numeric for clustering.")

# Step 2: Select features for clustering
X = df[[key2, key3]]  # Extract the numeric columns for clustering

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Initialize the K-means algorithm
df['Cluster'] = kmeans.fit_predict(X)  # Assign each data point to a cluster
