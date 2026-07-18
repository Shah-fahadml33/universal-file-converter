from pathlib import Path
from PIL import Image


def png_to_jpg(input_path: str, output_path: str, quality: int = 95):
    """
    Convert PNG to JPG.
    """

    image = Image.open(input_path).convert("RGB")
    image.save(output_path, "JPEG", quality=quality)

    return output_path


def jpg_to_png(input_path: str, output_path: str):
    """
    Convert JPG to PNG.
    """

    image = Image.open(input_path)
    image.save(output_path, "PNG")

    return output_path


def images_to_pdf(image_paths, output_path):
    """
    Convert multiple images into a single PDF.
    """

    if not image_paths:
        raise ValueError("No images provided.")

    images = []

    for path in image_paths:
        img = Image.open(path).convert("RGB")
        images.append(img)

    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:]
    )

    return output_path


def resize_image(
    input_path: str,
    output_path: str,
    width: int,
    height: int
):
    """
    Resize an image.
    """

    image = Image.open(input_path)

    resized = image.resize((width, height))

    resized.save(output_path)

    return output_path


def rotate_image(
    input_path: str,
    output_path: str,
    angle: int
):
    """
    Rotate an image.
    """

    image = Image.open(input_path)

    rotated = image.rotate(
        angle,
        expand=True
    )

    rotated.save(output_path)

    return output_path


def crop_image(
    input_path: str,
    output_path: str,
    left: int,
    top: int,
    right: int,
    bottom: int
):
    """
    Crop an image.
    """

    image = Image.open(input_path)

    cropped = image.crop(
        (
            left,
            top,
            right,
            bottom,
        )
    )

    cropped.save(output_path)

    return output_path


def grayscale_image(
    input_path: str,
    output_path: str
):
    """
    Convert image to grayscale.
    """

    image = Image.open(input_path)

    gray = image.convert("L")

    gray.save(output_path)

    return output_path


def compress_image(
    input_path: str,
    output_path: str,
    quality: int = 60
):
    """
    Compress an image.
    """

    image = Image.open(input_path)

    image.save(
        output_path,
        optimize=True,
        quality=quality,
    )

    return output_path


def get_image_info(input_path: str):
    """
    Return image metadata.
    """

    image = Image.open(input_path)

    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
        "format": image.format,
    }


def validate_image(input_path: str):
    """
    Check if the image is valid.
    """

    try:
        Image.open(input_path)
        return True
    except Exception:
        return False