import ffmpeg
from formats_hub.mp4 import to_mp4


def test_to_mp4(tmp_path):
    test_video_file = tmp_path / "test.mp4"
    output_file = tmp_path / "output.mp4"

    input_stream = ffmpeg.input("test.mp4")
    output_stream = ffmpeg.output(input_stream, str(test_video_file))
    ffmpeg.run(output_stream)

    result = to_mp4(str(test_video_file), str(output_file))
    assert result == str(output_file)

    converted = ffmpeg.probe(str(output_file))
    assert converted["format_name"] == "mp4"
    assert converted["duration"] == str(ffmpeg.probe(str(test_video_file))["duration"])
