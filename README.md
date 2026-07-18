# Universal File Converter

A Streamlit-based file converter supporting PDF, DOCX, Images, and PowerPoint.

## Features

### PDF

- PDF → DOCX
- PDF → PPTX
- PDF → PNG Images
- Merge PDFs
- Split PDFs
- Rotate PDFs
- Compress PDFs

### DOCX

- DOCX → PDF
- DOCX → TXT

### Images

- PNG → JPG
- JPG → PNG
- Images → PDF
- Resize Images
- Rotate Images
- Compress Images
- Crop Images
- Convert to Grayscale

### PowerPoint

- Images → PPTX
- Extract Slide Text
- Presentation Information

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/universal-file-converter.git
```

Move into the project

```bash
cd universal-file-converter
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Project Structure

```
universal-file-converter/
│
├── app.py
├── requirements.txt
├── README.md
│
├── converters/
│   ├── pdf_converter.py
│   ├── docx_converter.py
│   ├── image_converter.py
│   └── ppt_converter.py
│
└── utils/
    ├── file_utils.py
    ├── validation.py
    └── preview.py
```

---

## Requirements

- Python 3.10+
- Streamlit

---

## License

MIT License