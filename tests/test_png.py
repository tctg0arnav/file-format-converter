from PIL import Image
from formats_hub.png import to_png

def test_to_png(tmp_path):
    test_image_file = tmp_path / "test.jpg"
    output_file = tmp_path / "test.png"
    
    img = Image.new("RGB", (100, 100), color="red")
    img.save(test_image_file, "JPEG")
    
    result = to_png(str(test_image_file), str(output_file))
    assert result == str(output_file)
    
    converted = Image.open(output_file)
    assert converted.format == "PNG"
