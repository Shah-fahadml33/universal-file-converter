from pathlib import Path


SUPPORTED_CONVERSIONS = {
    ".pdf": [
        "DOCX",
        "PPTX",
        "PNG",
        "MERGE",
        "SPLIT",
        "ROTATE",
        "COMPRESS",
    ],
    ".docx": [
        "PDF",
        "TXT",
    ],
    ".png": [
        "JPG",
        "PDF",
    ],
    ".jpg": [
        "PNG",
        "PDF",
    ],
    ".jpeg": [
        "PNG",
        "PDF",
    ],
    ".pptx": [
        "INFO",
        "TEXT",
    ],
}


def file_exists(file_path):
    """
    Check if file exists.
    """

    return Path(file_path).exists()


def get_extension(file_path):
    """
    Return lowercase extension.
    """

    return Path(file_path).suffix.lower()


def is_supported_file(file_path):
    """
    Check whether file type is supported.
    """

    extension = get_extension(file_path)

    return extension in SUPPORTED_CONVERSIONS


def get_available_conversions(file_path):
    """
    Return valid conversions for a file.
    """

    extension = get_extension(file_path)

    return SUPPORTED_CONVERSIONS.get(extension, [])


def is_valid_conversion(file_path, target):
    """
    Validate requested conversion.
    """

    target = target.upper()

    return target in get_available_conversions(file_path)


def validate_file_size(file_path, max_size_mb=100):
    """
    Check maximum allowed size.
    """

    size = Path(file_path).stat().st_size

    return size <= max_size_mb * 1024 * 1024


def validate_multiple_files(file_paths):
    """
    Check whether all files exist.
    """

    return all(file_exists(file) for file in file_paths)


def validate_pdf(file_path):
    return get_extension(file_path) == ".pdf"


def validate_docx(file_path):
    return get_extension(file_path) == ".docx"


def validate_image(file_path):
    return get_extension(file_path) in [
        ".png",
        ".jpg",
        ".jpeg",
        ".bmp",
        ".gif",
        ".webp",
    ]


def validate_pptx(file_path):
    return get_extension(file_path) == ".pptx"


def validate_output_directory(directory):
    """
    Create output directory if needed.
    """

    path = Path(directory)

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return str(path)


def validate_filename(filename):
    """
    Remove illegal filename characters.
    """

    illegal = '<>:"/\\|?*'

    for char in illegal:
        filename = filename.replace(char, "_")

    return filename.strip()