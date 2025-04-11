import ffmpeg


def to_mp4(input_file, output_file):
    vid = ffmpeg.input(input_file)
    vid = ffmpeg.output(vid, output_file, vcodec="libx264", acodec="aac").run()
    return output_file
