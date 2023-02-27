from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key='ty test'
@app.route('/')
def index():
    return render_template("index.html")
           
@app.route('/form', methods=['POST'])
def form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True, port= 5100)
