from PIL import Image
from formats_hub.jpg import to_jpg

def test_to_jpg(tmp_path):
    test_image_file = tmp_path / "test.png"
    output_file = tmp_path / "test.jpg"
    
    img = Image.new("RGBA", (100, 100), color=(255, 0, 0, 128))
    img.save(test_image_file, "PNG")
    
    result = to_jpg(str(test_image_file), str(output_file))
    assert result == str(output_file)
    
    converted = Image.open(output_file)
    assert converted.format == "JPEG"
