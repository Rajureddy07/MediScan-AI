from rapidfuzz import fuzz
import pandas as pd

df = pd.read_csv("data/medicines.csv")

print("===== MEDICINES CSV DEBUG =====")
print(df.head())
print("Columns:", df.columns.tolist())
print("===============================")

medicine_list = df["medicine_name"].tolist()

def detect_medicine(text):

    text = text.upper()

    best_match = None
    best_score = 0

    for medicine in medicine_list:

        score = fuzz.partial_ratio(
            medicine.upper(),
            text
        )

        if score > best_score:
            best_score = score
            best_match = medicine

    if best_score > 70:
        return best_match, best_score

    return "Medicine Not Found", 0