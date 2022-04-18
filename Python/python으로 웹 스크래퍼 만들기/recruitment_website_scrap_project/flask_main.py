from flask import Flask


app = Flask("Scrapper")

@app.route("/")
def home():
  return "Hello welcome to youbin"

@app.route("/contact")
def contact():
  return "Contect me!"

app.run() # 서버 구축: http://127.0.0.1:5000

