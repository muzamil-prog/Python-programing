import numpy as np
import pandas as pd

# Sklearn imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
heart_data = pd.read_csv('heart.csv')

# Display dataset
print(heart_data.head())
print(heart_data.tail())

# Shape of dataset
print(heart_data.shape)

# Dataset information
heart_data.info()

# Splitting Features and Target
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

print(X)
print(Y)

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    stratify=Y,
    random_state=2
)

print(X.shape, X_train.shape, X_test.shape)

# Model Training
model = LogisticRegression(max_iter=1000)

model.fit(X_train, Y_train)

# Model Evaluation on Training Data
X_train_prediction = model.predict(X_train)

training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy on Training data : ', training_data_accuracy)

# Model Evaluation on Test Data
X_test_prediction = model.predict(X_test)

test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy on Test data : ', test_data_accuracy)