# K-Means Clustering Project

This project demonstrates the implementation of a K-Means clustering algorithm to group data based on user-provided inputs. The clustering is visualized using a scatter plot with centroids highlighted. Below is a breakdown of the project files and instructions for use.

## Files in the Project

### 1. `cluster.py`
This script performs the K-Means clustering process, including:
- Collecting data from the user.
- Applying the K-Means algorithm to cluster the data.
- Visualizing the clustering results.

#### Key Functions and Features:
- **`get_user_input`**: Prompts the user to select columns for clustering.
- **K-Means Clustering**: Assigns data points to clusters and calculates centroids.
- **Visualization**: Plots data points colored by cluster and displays centroids.

### 2. `dataset.py`
This script provides the `collect_data` function to gather input data for clustering.

#### Data Collection:
- **Labels (`key1`)**: Names or labels for the data points (e.g., city names).
- **Numeric Variables (`key2` and `key3`)**: Numeric values for clustering (e.g., sales figures).
- Ensures all input lists have the same length before returning a structured dataset.

## How to Run the Project

1. **Prepare the Environment**:
   - Install the required libraries:
     ```bash
     pip install pandas numpy matplotlib scikit-learn
     ```

2. **Run the Project**:
   - Execute the `cluster.py` script to start the clustering process.
     ```bash
     python cluster.py
     ```

3. **Provide Inputs**:
   - Enter labels (e.g., city names) and numeric data for clustering when prompted.
   - Select columns for clustering from the dataset.

4. **View Results**:
   - A scatter plot will be displayed, showing clustered data points and centroids.
   - Labels are annotated for clarity.

## Example Usage

### Input Example
```plaintext
Collecting data for cities, k2, and key3...
--------------------------------
Enter the name of the variable that you want to cluster: city
Enter a city name (or type 'e' to finish): CityA
Enter a city name (or type 'e' to finish): CityB
Enter a city name (or type 'e' to finish): e
Enter the name of the first variable that you want analyze: tomatoes
Enter a tomatoes value (or type 'e' to finish): 120
Enter a tomatoes value (or type 'e' to finish): 90
Enter a tomatoes value (or type 'e' to finish): e
Enter the name of the second variable that you want analyze: bread
Enter a bread value (or type 'e' to finish): 60
Enter a bread value (or type 'e' to finish): 70
Enter a bread value (or type 'e' to finish): e
```

### Output
- A scatter plot showing clusters of data points based on the provided numeric variables.
- Centroids of the clusters highlighted with red markers.

## Dependencies
- Python 3.x
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`

## Project Structure
```
.
├── cluster.py          # Main script for clustering and visualization
├── dataset.py          # Data collection script
├── README.md           # Project documentation (this file)
```

## Notes
- Ensure the data entered is consistent and numeric where required.
- K-Means clustering assumes that data is numeric and uses Euclidean distance for clustering.
- Modify the number of clusters (`n_clusters`) in the K-Means algorithm as needed.