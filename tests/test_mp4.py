import ffmpeg
from formats_hub.mp4 import to_mp4


def test_to_mp4(tmp_path):
    input_file = str(tmp_path / "input.avif")  # Convert to string
    ffmpeg.input("testsrc=size=128x128:rate=1", t=5, f="lavfi").output(
        input_file, vframes=1, format="avif"
    ).run()
    output_file = str(tmp_path / "output.mp4")  # Convert to string
    to_mp4(input_file, output_file)
    assert tmp_path.joinpath("output.mp4").exists()
    converted = ffmpeg.probe(output_file)
    assert any(
        stream["codec_type"] == "video" and stream["codec_name"] == "h264"
        for stream in converted["streams"]
    )
