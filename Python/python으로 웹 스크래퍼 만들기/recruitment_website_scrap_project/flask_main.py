from flask import Flask, render_template, request, redirect
from indeed import get_jobs

app = Flask("Scrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    jobs = get_jobs(word)
    print(jobs)
  else:
    return redirect("/")
  return render_template("report.html", searchingBy=word)

app.run() # 서버 구축: http://127.0.0.1:5000