# Scoring utility implementation
def compute_score(temp,humidity):
    score= 0
    if 18 <= temp <= 28:
        score +=5
    if humidity < 70:
        score +=3
    return score