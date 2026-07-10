import pandas as pd

df = pd.read_csv("data/medicines.csv")

def get_medicine_info(medicine_name):

    result = df[
        df["medicine_name"]
        .str.upper()
        == medicine_name.upper()
    ]

    if result.empty:
        return None

    return result.iloc[0]