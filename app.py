from flask import Flask, render_template, request
from baseline import create_baseline
from integrity_checker import check_integrity

app = Flask(__name__)
current_folder = "monitored"

@app.route("/")
def home():
    return render_template("index.html", folder=current_folder, scan=None, message=None)

@app.route("/set_folder", methods=["POST"])
def set_folder():
    global current_folder
    current_folder = request.form["folder"].strip()
    return render_template("index.html", folder=current_folder, scan=None,
                           message={"type": "success", "text": f"Folder set to: {current_folder}"})

@app.route("/baseline")
def baseline():
    msg = create_baseline(current_folder)
    return render_template("index.html", folder=current_folder, scan=None,
                           message={"type": "success", "text": msg})

@app.route("/check")
def check():
    scan = check_integrity(current_folder)
    return render_template("index.html", folder=current_folder, scan=scan, message=None)

if __name__ == "__main__":
    app.run(debug=True)