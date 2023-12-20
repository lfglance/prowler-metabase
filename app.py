from flask import Flask, render_template

import json

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def home():
    with open('output.json', 'r') as f:
        findings = json.loads(f.read())
        findings = findings[0:100]
    return render_template('home.html', findings=findings)

app.run()