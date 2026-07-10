import streamlit as st
import os
from models.history_manager import get_scan_history

st.title("📜 Scan History")

history = get_scan_history()

if history.empty:
    st.info("No scans available.")
else:
    st.dataframe(
        history.sort_values(
            by="timestamp",
            ascending=False
        ),
        use_container_width=True
    )

if st.button("🗑 Clear History"):

    if os.path.exists("data/scan_history.csv"):
        os.remove("data/scan_history.csv")

    st.success("History cleared.")
    st.rerun()