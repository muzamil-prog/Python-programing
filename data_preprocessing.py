import pandas as pd


class DataPreprocessing:

    def loadData(self):

        df = pd.read_csv("data/students.csv")

        return df


    def prepareData(self):

        df = self.loadData()

        X = df[["math", "computer", "Ai"]]

        y = df["status"]

        return X, y