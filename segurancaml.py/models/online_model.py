import numpy as np
from sklearn.linear_model import SGDClassifier

class OnlineDefensiveModel:
    def __init__(self):
        self.model = SGDClassifier(
            loss="log_loss",
            learning_rate="optimal",
            random_state=42
        )
        self.initialized = False

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def update(self, X, y):
        if not self.initialized:
            self.model.partial_fit(X, y, classes=np.array([0, 1]))
            self.initialized = True
        else:
            self.model.partial_fit(X, y)

