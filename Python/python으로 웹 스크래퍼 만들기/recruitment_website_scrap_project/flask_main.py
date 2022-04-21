from flask import Flask, render_template, request


app = Flask("Scrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  return render_template("report.html", searchingBy=word)

app.run() # 서버 구축: http://127.0.0.1:5000