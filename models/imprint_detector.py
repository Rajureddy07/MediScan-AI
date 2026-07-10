import pandas as pd
from rapidfuzz import fuzz

df = pd.read_csv("data/imprint_codes.csv")

def detect_imprint(text):

    text = text.upper()

    best_match = None
    best_score = 0

    for _, row in df.iterrows():

        imprint = str(row["imprint_code"]).upper()

        score = fuzz.partial_ratio(
            imprint,
            text
        )

        if score > best_score:
            best_score = score
            best_match = row["medicine_name"]

    if best_score > 99:
        return best_match

    return None