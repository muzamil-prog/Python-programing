import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from ml.data_preprocessing import DataPreprocessing


class TrainModel:

    def __init__(self):
        self.model = None
        self.accuracy = None

    def trainModel(self):

        preprocessing = DataPreprocessing()

        X, y = preprocessing.prepareData()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model = LogisticRegression()

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        self.accuracy = accuracy_score(y_test, predictions)

        return self.accuracy

    def predict(self, math, computer, ai):

        if self.model is None:
            return "Please train the AI Model first."

        prediction = self.model.predict([[math, computer, ai]])

        return prediction[0]
    
    def saveModel(self):

         if self.model is None:
             print("Please train the model first.")
             return

         joblib.dump(self.model, "models/model.pkl")

         print("Model saved successfully.")
    def loadModel(self):

         model_path = "models/model.pkl"

         if os.path.exists(model_path):

             self.model = joblib.load(model_path)

             print("Model Loaded Successfully.")

             return True

         else:

             print("No Saved Model Found.")

             return False     