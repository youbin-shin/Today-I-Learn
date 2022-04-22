from flask import Flask, render_template, request, redirect
from indeed import get_jobs

app = Flask("Scrapper")

# fake db
db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    fromDb = db.get(word)
    if fromDb:
      jobs = fromDb
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html",
    searchingBy=word,
    resultsNumber = len(jobs)
  )

app.run() # 서버 구축: http://127.0.0.1:5000