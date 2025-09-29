import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load your dataset into a pandas DataFrame
data = pd.read_csv(
    "/Users/borislo830/Desktop/Uber Hackathon Study Case/analysis/encoded_data.csv", encoding='latin-1')

# Select the independent variables (features) and the dependent variable (target)
X = data[['country_CHN']]
y = data['primary_fuel_Coal']

# Create a linear regression model
model = LinearRegression()

# Perform k-fold cross-validation predictions
y_cv_pred = cross_val_predict(model, X, y, cv=5)

# Calculate Mean Squared Error for cross-validation predictions
cv_mse = mean_squared_error(y, y_cv_pred)

# Fit the model on the entire dataset
model.fit(X, y)

# Make predictions on the entire dataset
y_pred = model.predict(X)

# Calculate Mean Squared Error for the entire dataset
mse = mean_squared_error(y, y_pred)

# Calculate R-squared value
r2 = r2_score(y, y_pred)

# Plot the cross-validation predictions and actual values
plt.figure(figsize=(10, 6))
plt.scatter(y, y_cv_pred, color='blue', label='Cross-Validation Predictions')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red',
         linestyle='--', linewidth=2, label='Perfect Fit')
plt.xlabel('Actual GDP')
plt.ylabel('Predicted GDP (Cross-Validation)')
plt.title('Actual vs. Predicted GDP (Cross-Validation)')
plt.legend()
plt.show()

# Plot the entire dataset predictions and actual values
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, color='green', label='Predictions')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red',
         linestyle='--', linewidth=2, label='Perfect Fit')
plt.xlabel('Actual GDP')
plt.ylabel('Predicted GDP')
plt.title('Actual vs. Predicted GDP')
plt.legend()
plt.show()

# Print Mean Squared Error
print("Cross-Validation MSE:", cv_mse)
print("MSE:", mse)
print("R-squared:", r2)
