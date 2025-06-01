from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/equipe')
def ola_equipe():
    return render_template('equipe.html')

app.run()