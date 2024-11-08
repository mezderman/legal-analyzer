from flask import Flask, render_template, request, redirect, url_for
from utils.ocr import extract_text_from_pdf
from utils.llm_analysis import analyze_text_with_llm
from utils.json_cleaner import clean_and_parse_json
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            return redirect(url_for("analyze", filename=file.filename))
    return render_template("index.html")

@app.route("/analyze/<filename>")
def analyze(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    text = extract_text_from_pdf(filepath)
    llm_response = analyze_text_with_llm(text)
    result = clean_and_parse_json(llm_response)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
