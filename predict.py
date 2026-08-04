class PredictStudent:

    def __init__(self, trainer):

        self.trainer = trainer

    def predictResult(self, math, computer, ai):

        return self.trainer.predict(
            math,
            computer,
            ai
        )