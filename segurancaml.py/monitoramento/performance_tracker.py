class PerformanceTracker:
    def __init__(self):
        self.total = 0
        self.correct = 0

    def update(self, prediction, label):
        self.total += 1
        if prediction == label:
            self.correct += 1

    def accuracy(self):
        return self.correct / self.total if self.total > 0 else 0
