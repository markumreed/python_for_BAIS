# Linear Regression with Sklearn Tutorial

## Introduction

Linear regression is a fundamental statistical technique used to model the relationship between a dependent variable and one or more independent variables. In this tutorial, you will learn how to perform linear regression using the Scikit-Learn (sklearn) library in Python.

### Prerequisites
- Basic understanding of Python programming
- Basic understanding of linear regression concepts
- Python and necessary libraries installed (numpy, pandas, matplotlib, scikit-learn)

## 1. Setting Up the Environment

### Step 1: Install Required Libraries

If you haven't already installed the necessary libraries, you can do so using pip:
```bash
pip install numpy pandas matplotlib scikit-learn
```

### Step 2: Import Libraries

Create a new Python script or Jupyter Notebook and import the required libraries:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
```

## 2. Load and Prepare the Data

For this tutorial, we will use a sample dataset. You can use any dataset suitable for linear regression. For demonstration purposes, let's create a simple synthetic dataset:

```python
# Generate a synthetic dataset
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Convert to a DataFrame
data = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})
print(data.head())
```

## 3. Data Visualization

Before building the model, it's a good practice to visualize the data to understand its distribution and relationships:

```python
plt.scatter(data['X'], data['y'])
plt.xlabel('X')
plt.ylabel('y')
plt.title('Scatter plot of X vs y')
plt.show()
```

## 4. Split the Data

Split the data into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```

## 5. Build and Train the Model

Create a Linear Regression model and train it on the training data:

```python
# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
```

## 6. Make Predictions

Use the trained model to make predictions on the test data:

```python
# Make predictions
y_pred = model.predict(X_test)
```

## 7. Evaluate the Model

Evaluate the model's performance using metrics such as Mean Squared Error (MSE) and R-squared (R²):

```python
# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
```

## 8. Visualize the Results

Visualize the model's predictions compared to the actual data:

```python
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Actual vs Predicted values')
plt.legend()
plt.show()
```

## 9. Model Coefficients

You can also access the model's coefficients (slope and intercept):

```python
print(f"Intercept: {model.intercept_[0]}")
print(f"Coefficient: {model.coef_[0][0]}")
```

## 10. Conclusion

By following this tutorial, you've learned how to perform linear regression using Scikit-Learn. You've created a synthetic dataset, visualized the data, built and trained a model, made predictions, evaluated the model's performance, and visualized the results. This foundational knowledge will enable you to apply linear regression to real-world datasets and build more complex models.

Happy coding!