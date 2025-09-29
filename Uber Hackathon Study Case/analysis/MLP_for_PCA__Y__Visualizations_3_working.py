import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import shap

# Read data from CSV file
data = pd.read_csv(
    '/Users/borislo830/Desktop/Uber Hackathon Study Case/analysis/encoded_data.csv')

# Get the column names separated by commas
column_names = ', '.join(data.columns)

# Convert the comma-separated string to a list of column names
column_names_list = column_names.split(', ')

# Drop the 'extracted_gdp' column from the list
column_names_list.remove('extracted_gdp')


# Select the variables for correlation with principal components
variables = column_names_list

# Perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data[variables])

# Extract PC1 and PC2 from the principal components
PC1 = principal_components[:, 0]
PC2 = principal_components[:, 1]

# Add PC1 and PC2 as columns to the dataset
data['PC1'] = PC1
data['PC2'] = PC2

# Define the predictors (PC1 and PC2) and the target variable (extracted_gdp)
X = data[['PC1', 'PC2']]
y = data['extracted_gdp']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Standardize the target variable (extracted_gdp)
scaler_target = StandardScaler()
y_train_scaled = scaler_target.fit_transform(y_train.values.reshape(-1, 1))
y_test_scaled = scaler_target.transform(y_test.values.reshape(-1, 1))

# Build your neural network model with dropout and L2 regularization
model = keras.Sequential([
    keras.layers.Input(shape=(X_train_scaled.shape[1],)),
    keras.layers.Dense(128, activation='relu',
                       kernel_regularizer=keras.regularizers.l2(0.001)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu',
                       kernel_regularizer=keras.regularizers.l2(0.001)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(1)
])

# Compile the model
model.compile(loss='mse', optimizer='adam')

# Train the model with early stopping
early_stopping = keras.callbacks.EarlyStopping(
    patience=10, restore_best_weights=True)
history = model.fit(X_train_scaled, y_train_scaled, validation_split=0.2, epochs=100, batch_size=32,
                    callbacks=[early_stopping], verbose=1)

# Evaluate the model
y_pred_scaled = model.predict(X_test_scaled)
y_pred = scaler_target.inverse_transform(y_pred_scaled)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)

# Prediction vs Ground Truth Plot with Regression Line
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot(np.unique(y_test), np.poly1d(np.polyfit(
    y_test, y_pred[:, 0], 1))(np.unique(y_test)), color='r')
plt.xlabel('Actual GDP')
plt.ylabel('Predicted GDP')
plt.title('Predicted vs. Actual GDP')
plt.text(0.05, 0.9, f'R-squared = {r2:.2f}', transform=plt.gca().transAxes)
plt.show()
'''
# Heatmap
data_corr = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(data_corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
'''
# SHAP Feature Importance
explainer = shap.Explainer(model, X_train_scaled)
shap_values = explainer(X_test_scaled)
shap.summary_plot(shap_values, X_test_scaled, feature_names=X.columns)
