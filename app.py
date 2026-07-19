import os
from pathlib import Path

import streamlit as st

from converters.pdf_converter import (
    pdf_to_docx,
    pdf_to_pptx,
    pdf_to_images,
    merge_pdfs,
    split_pdf,
    rotate_pdf,
    compress_pdf,
)

from converters.docx_converter import (
    docx_to_pdf,
    docx_to_txt,
)

from converters.image_converter import (
    png_to_jpg,
    jpg_to_png,
    images_to_pdf,
)

from converters.ppt_converter import (
    extract_slide_text,
    get_presentation_info,
)

from utils.file_utils import (
    create_temp_directory,
    save_uploaded_file,
    get_extension,
)

from utils.validation import (
    get_available_conversions,
    is_supported_file,
)

from utils.preview import preview


st.set_page_config(
    page_title="Universal File Converter",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Universal File Converter")

uploaded = st.file_uploader(
    "Upload File",
    type=[
        "pdf",
        "docx",
        "png",
        "jpg",
        "jpeg",
        "pptx",
    ],
)

if uploaded is not None:

    with create_temp_directory() as temp:

        input_path = save_uploaded_file(uploaded, temp)

        st.divider()

        st.subheader("Preview")

        preview(input_path)

        st.divider()

        extension = get_extension(input_path)

        if not is_supported_file(input_path):
            st.error("Unsupported file type.")
            st.stop()

        options = get_available_conversions(input_path)

        option = st.selectbox(
            "Convert To",
            options,
        )

        if st.button("Convert"):

            progress = st.progress(0)

            output_folder = Path(temp) / "output"
            output_folder.mkdir(exist_ok=True)

            output_file = None

            try:

                progress.progress(20)

                # ---------------- PDF ----------------

                if extension == ".pdf":

                    if option == "DOCX":

                        output_file = output_folder / "converted.docx"

                        pdf_to_docx(
                            input_path,
                            str(output_file),
                        )

                    elif option == "PPTX":

                        output_file = output_folder / "converted.pptx"

                        pdf_to_pptx(
                            input_path,
                            str(output_file),
                        )

                    elif option == "PNG":

                        image_folder = output_folder / "images"

                        images = pdf_to_images(
                            input_path,
                            str(image_folder),
                        )

                        import zipfile

                        zip_path = output_folder / "images.zip"

                        with zipfile.ZipFile(zip_path, "w") as zipf:
                            for image in images:
                                zipf.write(image, Path(image).name)

                        output_file = zip_path

                    elif option == "SPLIT":

                        split_folder = output_folder / "split"

                        pdfs = split_pdf(
                            input_path,
                            str(split_folder),
                        )

                        import zipfile

                        zip_path = output_folder / "split_pdf.zip"

                        with zipfile.ZipFile(zip_path, "w") as zipf:
                            for pdf in pdfs:
                                zipf.write(pdf, Path(pdf).name)

                        output_file = zip_path

                    elif option == "ROTATE":

                        output_file = output_folder / "rotated.pdf"

                        rotate_pdf(
                            input_path,
                            str(output_file),
                            rotation=90,
                        )

                    elif option == "COMPRESS":

                        output_file = output_folder / "compressed.pdf"

                        compress_pdf(
                            input_path,
                            str(output_file),
                        )

                    elif option == "MERGE":

                        st.info(
                            "Merge requires multiple PDF uploads. "
                            "Current uploader accepts only one file."
                        )

                        st.stop()
                # ---------------- DOCX ----------------

                elif extension == ".docx":

                    if option == "PDF":

                        output_file = output_folder / "converted.pdf"

                        docx_to_pdf(
                            input_path,
                            str(output_file),
                        )

                    elif option == "TXT":

                        output_file = output_folder / "converted.txt"

                        docx_to_txt(
                            input_path,
                            str(output_file),
                        )

                # ---------------- PNG ----------------

                elif extension == ".png":

                    if option == "JPG":

                        output_file = output_folder / "converted.jpg"

                        png_to_jpg(
                            input_path,
                            str(output_file),
                        )

                    elif option == "PDF":

                        output_file = output_folder / "converted.pdf"

                        images_to_pdf(
                            [input_path],
                            str(output_file),
                        )

                # ---------------- JPG ----------------

                elif extension in [".jpg", ".jpeg"]:

                    if option == "PNG":

                        output_file = output_folder / "converted.png"

                        jpg_to_png(
                            input_path,
                            str(output_file),
                        )

                    elif option == "PDF":

                        output_file = output_folder / "converted.pdf"

                        images_to_pdf(
                            [input_path],
                            str(output_file),
                        )

                # ---------------- PPTX ----------------

                elif extension == ".pptx":

                    if option == "INFO":

                        info = get_presentation_info(
                            input_path
                        )

                        st.json(info)

                        st.stop()

                    elif option == "TEXT":

                        text = extract_slide_text(
                            input_path
                        )

                        st.text_area(
                            "Presentation Text",
                            text,
                            height=400,
                        )

                        st.stop()

                progress.progress(100)

                st.success("Conversion Successful!")

                if output_file is not None:

                    with open(output_file, "rb") as f:

                        st.download_button(
                            "⬇ Download",
                            f,
                            file_name=output_file.name,
                        )

            except Exception as e:

                st.error(str(e))