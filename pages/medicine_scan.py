import streamlit as st
import tempfile

from models.medicine_detector import detect_medicine
from models.medicine_info import get_medicine_info
from models.ocr_engine import extract_text
from models.text_cleaner import clean_text
from models.image_preprocessor import preprocess_image
from models.imprint_detector import detect_imprint
from models.history_manager import save_scan

st.title("💊 MediScan AI")

st.write("""
Upload:
- Full Medicine Strips
- Partial/Cut Strips
- Pills with Imprint Codes
""")

uploaded_file = st.file_uploader(
    "Upload Medicine Strip / Pill Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp_file:

        temp_file.write(uploaded_file.read())
        image_path = temp_file.name

    with st.spinner("Analyzing Medicine..."):

        # Original OCR
        original_text = extract_text(image_path)

        # Processed OCR
        processed_image = preprocess_image(image_path)
        processed_text = extract_text(processed_image)

        # Select better OCR result
        if len(processed_text) > len(original_text):
            extracted_text = processed_text
            ocr_source = "Processed Image"
        else:
            extracted_text = original_text
            ocr_source = "Original Image"

        cleaned_text = clean_text(extracted_text)

        # Medicine Detection
        medicine_name, confidence = detect_medicine(
            cleaned_text
        )

        detection_method = "Medicine Name Detection"

        # Pill Imprint Detection
        if medicine_name == "Medicine Not Found":

            imprint_result = detect_imprint(
                cleaned_text
            )

            if imprint_result:

                medicine_name = imprint_result
                confidence = 80
                detection_method = "Pill Imprint Detection"

        # Save successful scans
        if medicine_name != "Medicine Not Found":
            save_scan(
                medicine_name,
                confidence
            )

        medicine_info = get_medicine_info(
            medicine_name
        )

    st.subheader("Detected Medicine")

    if medicine_name != "Medicine Not Found":

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Medicine",
                medicine_name
            )

        with col2:
            st.metric(
                "Confidence",
                f"{confidence:.1f}%"
            )

        st.success(
            f"Detected using: {detection_method}"
        )

        if medicine_info is not None:

            st.subheader("Medicine Information")

            st.info(
                f"""
Generic Name: {medicine_info['generic_name']}

Uses: {medicine_info['uses']}

Side Effects: {medicine_info['side_effects']}

Category: {medicine_info['category']}
"""
            )

    else:

        st.error("Medicine Not Found")

    # Technical Details

    with st.expander("🔍 Technical Details"):

        st.write(f"Best OCR Source: {ocr_source}")

        st.subheader("Original OCR")
        st.write(original_text)

        st.subheader("Processed OCR")
        st.write(processed_text)

        st.subheader("Final OCR Used")
        st.write(extracted_text)

        st.subheader("Cleaned Text")
        st.success(cleaned_text)