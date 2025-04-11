from PIL import Image


def to_jpg(input_file, output_file):
    img = Image.open(input_file)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save(output_file, "jpeg")
    return output_file
