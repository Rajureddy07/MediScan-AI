import pandas as pd
from datetime import datetime
import os

HISTORY_FILE = "data/scan_history.csv"

def save_scan(medicine_name, confidence):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    new_record = pd.DataFrame([{
        "timestamp": timestamp,
        "medicine_name": medicine_name,
        "confidence": confidence
    }])

    if os.path.exists(HISTORY_FILE):
        new_record.to_csv(
            HISTORY_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        new_record.to_csv(
            HISTORY_FILE,
            index=False
        )

def get_scan_history():

    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)

    return pd.DataFrame(
        columns=[
            "timestamp",
            "medicine_name",
            "confidence"
        ]
    )