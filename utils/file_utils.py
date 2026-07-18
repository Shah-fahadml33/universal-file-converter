import os
import shutil
import tempfile
import zipfile
from pathlib import Path
from uuid import uuid4


def create_temp_directory():
    """
    Create and return a temporary directory.
    """

    return tempfile.TemporaryDirectory()


def save_uploaded_file(uploaded_file, directory):
    """
    Save a Streamlit uploaded file.
    """

    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    file_path = directory / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return str(file_path)


def copy_file(source, destination):
    """
    Copy a file.
    """

    destination = Path(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source, destination)

    return str(destination)


def move_file(source, destination):
    """
    Move a file.
    """

    destination = Path(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.move(source, destination)

    return str(destination)


def delete_file(file_path):
    """
    Delete a file.
    """

    file = Path(file_path)

    if file.exists():
        file.unlink()


def delete_folder(folder_path):
    """
    Delete a folder recursively.
    """

    folder = Path(folder_path)

    if folder.exists():
        shutil.rmtree(folder)


def get_extension(file_path):
    """
    Return file extension.
    """

    return Path(file_path).suffix.lower()


def get_filename(file_path):
    """
    Return filename without extension.
    """

    return Path(file_path).stem


def generate_unique_filename(extension):
    """
    Generate a unique filename.
    """

    extension = extension.replace(".", "")

    return f"{uuid4().hex}.{extension}"


def ensure_directory(directory):
    """
    Create directory if it doesn't exist.
    """

    Path(directory).mkdir(
        parents=True,
        exist_ok=True
    )


def format_file_size(size):
    """
    Convert bytes into readable text.
    """

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB"
    ]

    for unit in units:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


def create_zip(files, output_zip):
    """
    Create a ZIP archive.
    """

    with zipfile.ZipFile(
        output_zip,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for file in files:

            zipf.write(
                file,
                arcname=os.path.basename(file)
            )

    return output_zip


def list_files(directory):
    """
    Return all files inside a directory.
    """

    return [
        str(file)
        for file in Path(directory).iterdir()
        if file.is_file()
    ]


def get_file_size(file_path):
    """
    Return file size in bytes.
    """

    return os.path.getsize(file_path)


def is_supported(file_path, extensions):
    """
    Check whether the file extension is supported.
    """

    return get_extension(file_path) in extensions