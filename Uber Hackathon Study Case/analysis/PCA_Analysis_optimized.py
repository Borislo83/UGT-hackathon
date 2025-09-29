from sklearn.decomposition import IncrementalPCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2023)

# Read the CSV file
# Replace 'YourDataset.csv' with your actual dataset file
X = pd.read_csv(
    '/Users/borislo830/Desktop/Uber Hackathon Study Case/analysis/encoded_data.csv')

# Convert categorical variables to one-hot encoded format
X_encoded = pd.get_dummies(X)

# Transpose the dataset to have variables in columns
X_transposed = X_encoded.T

# Determine the batch size based on memory constraints
# You can adjust this value based on available memory
batch_size = 1000

# Initialize IncrementalPCA and fit the data in batches
n_components = 10  # Choose the number of principal components you want
ipca = IncrementalPCA(n_components=n_components, batch_size=batch_size)

# Convert the transposed dataframe to numpy array for batching
X_array = X_transposed.values

# Fit the data in batches
num_batches = X_array.shape[0] // batch_size + 1
for i in range(num_batches):
    batch = X_array[i * batch_size: (i + 1) * batch_size, :]
    ipca.partial_fit(batch)

# Access the explained variance ratio
explained_var_ratio = ipca.explained_variance_ratio_

# Create scree plot
num_components = len(explained_var_ratio)
plt.plot(range(1, num_components + 1), explained_var_ratio, 'bo-')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Scree Plot')

# Add percentage labels
for i, ratio in enumerate(explained_var_ratio):
    plt.text(i + 1, ratio + 0.01, f'{ratio*100:.2f}%', ha='center')

plt.xticks(range(1, num_components + 1))
plt.show()
