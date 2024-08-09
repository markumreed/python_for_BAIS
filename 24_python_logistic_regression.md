# Logistic Regression with Sklearn Tutorial

## Introduction

Logistic regression is a statistical method for predicting binary outcomes. It is used when the dependent variable is categorical and is particularly useful for classification problems. In this tutorial, you will learn how to perform logistic regression using the Scikit-Learn (sklearn) library in Python.

### Prerequisites
- Basic understanding of Python programming
- Basic understanding of logistic regression concepts
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

## 2. Load and Prepare the Data

For this tutorial, we will use a sample dataset. You can use any dataset suitable for logistic regression. For demonstration purposes, let's create a simple synthetic dataset:

```python
# Generate a synthetic dataset
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Convert to a DataFrame
data = pd.DataFrame({'X1': X[:, 0], 'X2': X[:, 1], 'y': y})
print(data.head())
```

## 3. Data Visualization

Before building the model, it's a good practice to visualize the data to understand its distribution and relationships:

```python
plt.scatter(data[data['y'] == 0]['X1'], data[data['y'] == 0]['X2'], color='red', label='Class 0')
plt.scatter(data[data['y'] == 1]['X1'], data[data['y'] == 1]['X2'], color='blue', label='Class 1')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Scatter plot of X1 vs X2')
plt.legend()
plt.show()
```

## 4. Split the Data

Split the data into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```

## 5. Build and Train the Model

Create a Logistic Regression model and train it on the training data:

```python
# Create the model
model = LogisticRegression()

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

Evaluate the model's performance using metrics such as Accuracy, Confusion Matrix, and Classification Report:

```python
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)
```

## 8. Visualize the Results

Visualize the decision boundary of the logistic regression model:

```python
# Define the decision boundary
xx, yy = np.mgrid[-3:3:.01, -3:3:.01]
grid = np.c_[xx.ravel(), yy.ravel()]
probs = model.predict_proba(grid)[:, 1].reshape(xx.shape)

# Plot the decision boundary
plt.scatter(data[data['y'] == 0]['X1'], data[data['y'] == 0]['X2'], color='red', label='Class 0')
plt.scatter(data[data['y'] == 1]['X1'], data[data['y'] == 1]['X2'], color='blue', label='Class 1')
plt.contour(xx, yy, probs, levels=[.5], cmap="Greys", vmin=0, vmax=.6)

plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Decision Boundary')
plt.legend()
plt.show()
```

## Conclusion

By following this tutorial, you've learned how to perform logistic regression using Scikit-Learn. You've created a synthetic dataset, visualized the data, built and trained a model, made predictions, evaluated the model's performance, and visualized the results. This foundational knowledge will enable you to apply logistic regression to real-world classification problems and build more complex models.

Happy coding!