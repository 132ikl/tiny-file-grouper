from flask import Flask, request
from flask_httpauth import HTTPDigestAuth
import io
import tarfile
import os
import shutil

app = Flask(__name__)
app.config["SECRET_KEY"] = "REPLACE_ME"
auth = HTTPDigestAuth()

users = {"user": "password"}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route("/<group>/<filename>", methods=["PUT"])
@auth.login_required
def upload(group, filename):
    os.makedirs(os.path.join("files", group), exist_ok=True)
    with open(os.path.join("files", group, filename), "wb") as f:
        f.write(request.data)
    return "File uploaded"


@app.route("/download/<group>")
@auth.login_required
def download(group):
    dlfile = io.BytesIO()
    path = os.path.join("files", group)
    if os.path.exists(path):
        with tarfile.open(mode="w:gz", fileobj=dlfile) as tar:
            for i in os.listdir(path):
                filepath = os.path.join(path, i)
                tar.add(filepath, arcname=os.path.basename(filepath))
        shutil.rmtree(path)
        return dlfile.getvalue()
    return "File not found"


if __name__ == "__main__":
    app.run()
