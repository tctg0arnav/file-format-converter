import ffmpeg
from formats_hub.mp4 import to_mp4


def test_to_mp4(tmp_path):
    input_file = tmp_path / "input.avif"
    ffmpeg.input("testsrc=size=128x128:rate=1", duration=5).output(
        str(input_file), vframes=1, format="avif"
    ).run()
    output_file = tmp_path / "output.mp4"
    to_mp4(input_file, output_file)
    assert output_file.exists()
    converted = ffmpeg.probe(str(output_file))
    assert any(
        stream["codec_type"] == "video" and stream["codec_name"] == "h264"
        for stream in converted["streams"]
    )
    assert any(
        stream["codec_type"] == "audio" and stream["codec_name"] == "aac"
        for stream in converted["streams"]
    )
    assert converted["format_name"] == "mp4"
