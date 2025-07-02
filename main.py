from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    first_choice = request.form.get('first_choice')  # Handles HIYYYAAAA / hello
    answer = request.form.get('answer')              # Handles YES / NO
    return render_template("index.html", choice=first_choice, answer=answer)

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
