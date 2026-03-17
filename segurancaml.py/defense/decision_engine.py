def decide(prediction, probability):
    if prediction == 1 and probability > 0.8:
        return "BLOCK"
    elif prediction == 1:
        return "ALERT"
    else:
        return "ALLOW"
