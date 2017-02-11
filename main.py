import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

# app configuration
app = Flask(__name__)
app.debug = False
PORT = 8080

# routing
@app.route("/")
def homePage():
  return render_template("index.html")

# start the app if we're directly running this file
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = PORT)
