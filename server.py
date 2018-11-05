from flask import Flask, render_template, request, redirect, flash, session
import re

app = Flask(__name__)
app.secret_key = 'lol'

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/result", methods=["post"])
def result():
    if len(request.form['name']) < 1 or len(request.form['comment']) < 1:
        flash('You cannot leave this blank!')
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash('Please do not enter more than 120 characters in this comment box!')
        return redirect('/')
    else:
        return render_template('return.html', names=request.form["name"], locations= request.form["location"], favorite=request.form["fav_lang"], comments=request.form["comment"])

@app.route("/danger")
def danger():
    print("A user tried to visit /danger. We have redirected the user to '/'")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
