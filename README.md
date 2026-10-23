# MediScan AI

[![Python syntax](https://github.com/Rajureddy07/MediScan-AI/actions/workflows/syntax.yml/badge.svg)](https://github.com/Rajureddy07/MediScan-AI/actions/workflows/syntax.yml)

An OCR-assisted medicine-name recognition prototype that helps a user search for likely medicine-name matches from package images. The project combines image preprocessing, text extraction, and fuzzy string matching in a Streamlit interface.

> **Safety notice:** This is an educational prototype, not a medical device. OCR and fuzzy matches can be wrong. Never use its output to identify, select, dose, or take medication without confirmation from a pharmacist or other qualified healthcare professional. Do not upload private patient information.

## Capabilities

- Extract visible text from medicine-package images using EasyOCR.
- Preprocess images with OpenCV to improve text extraction.
- Compare extracted text against a medicine reference CSV using RapidFuzz.
- Browse the local reference data and view recent scan history.
- Use a Streamlit web interface for scan, search, and history workflows.

Recognition quality depends on image clarity, text orientation, lighting, package damage, and the completeness of the reference data. Similar names are not proof that two products are equivalent.

## Technology

Python · Streamlit · EasyOCR · OpenCV · Pandas · RapidFuzz

## Repository layout

```text
.
├── app.py
├── pages/
│   ├── medicine_scan.py
│   ├── medicine_search.py
│   ├── scan_history.py
│   └── chatbot.py
├── models/
│   ├── ocr_engine.py
│   ├── image_preprocessor.py
│   ├── medicine_detector.py
│   ├── medicine_info.py
│   ├── imprint_detector.py
│   ├── text_cleaner.py
│   └── history_manager.py
├── data/
│   ├── medicines.csv
│   ├── imprint_codes.csv
│   └── scan_history.csv
├── requirements.txt
└── test_ocr.py
```

## Run locally

Use Python 3.10 or a version supported by the installed dependency versions.

```bash
git clone https://github.com/Rajureddy07/MediScan-AI.git
cd MediScan-AI
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and start Streamlit:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The first EasyOCR run may download model weights, so the initial start can take longer and may require an internet connection. Streamlit prints the local URL in the terminal.

## Reference data

The app uses CSV files under `data/`. Review their column names and provenance before replacing or extending them. Do not treat a local reference CSV as a complete or authoritative medicine database.

## Development and validation

- `test_ocr.py` is the current OCR smoke-test entry point; run it according to its code and the local OCR environment.
- Test using non-sensitive sample images and manually verify extracted strings.
- Record false positives and false negatives before making claims about accuracy.
- Keep dependency versions and model artifacts documented when sharing reproducible results.

## Author

G. Rajasekhar Reddy · [GitHub](https://github.com/Rajureddy07)
