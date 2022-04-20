from flask import Flask, render_template


app = Flask("Scrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/<username>")
def hello(username):
  return f"Hello {username}!"

app.run() # 서버 구축: http://127.0.0.1:5000

