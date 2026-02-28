def evaluate_confidence(distance):
    if distance < 1.15:
        return "High"
    elif distance < 1.25:
        return "Medium"
    else:
        return "Low"