from PIL import Image

def to_png(input_file, output_file):
    img = Image.open(input_file)
    img.save(output_file, 'png')
    return output_file