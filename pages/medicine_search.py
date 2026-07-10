import streamlit as st
import pandas as pd
import os

st.title("🔍 Medicine Search")

csv_path = os.path.join(
    "data",
    "medicines.csv"
)
df = pd.read_csv(csv_path)
medicine_name = st.text_input(
    "Enter Medicine Name"
)

if medicine_name:

    result = df[
        df["medicine_name"]
        .str.upper()
        .str.contains(
            medicine_name.upper(),
            na=False
        )
    ]

    if not result.empty:

        st.success("Medicine Found")

        for _, row in result.iterrows():

            st.subheader(
                row["medicine_name"]
            )

            st.write(
                f"**Generic Name:** {row['generic_name']}"
            )

            st.write(
                f"**Uses:** {row['uses']}"
            )

            st.write(
                f"**Side Effects:** {row['side_effects']}"
            )

            st.write(
                f"**Category:** {row['category']}"
            )

    else:

        st.error(
            "Medicine Not Found"
        )