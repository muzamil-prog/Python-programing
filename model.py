import numpy as np
import pandas as pd

# Sklearn imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
student_data = pd.read_csv('student-mat.csv', sep=';')

# Display dataset
print(student_data.head())
print(student_data.tail())

# Shape of dataset
print(student_data.shape)

# Dataset information
student_data.info()

# Convert categorical columns into numeric
le = LabelEncoder()

for column in student_data.select_dtypes(include='object').columns:
    student_data[column] = le.fit_transform(student_data[column])

# Create target column (Pass = 1, Fail = 0)
student_data['target'] = (student_data['G3'] >= 10).astype(int)

# Splitting Features and Target
X = student_data.drop(columns=['G3', 'target'], axis=1)
Y = student_data['target']

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