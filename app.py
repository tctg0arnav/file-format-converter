from flask import Flask, request, url_for, send_file, render_template
from formats_hub import png, jpg, mp4
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "avif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    shutil.rmtree(app.config["UPLOAD_FOLDER"])
    shutil.os.mkdir(app.config["UPLOAD_FOLDER"])
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = file.filename
            output_name = filename.split(".")[0]
            if request.form.get("convertto") == "png":
                filepath = png.to_png(
                    file, f'{app.config["UPLOAD_FOLDER"]}/{output_name}.png'
                )
            elif request.form.get("convertto") == "jpg":
                filepath = jpg.to_jpg(
                    file, f'{app.config["UPLOAD_FOLDER"]}/{output_name}.jpg'
                )
            elif request.form.get("convertto") == "mp4":
                filepath = mp4.to_mp4(
                    file, f'{app.config["UPLOAD_FOLDER"]}/{output_name}.mp4'
                )
            return send_file(filepath, as_attachment=True)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
