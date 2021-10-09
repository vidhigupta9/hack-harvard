from flask import Flask, render_template, request, redirect , url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('searchresults.html',Heading = "hey",Summary= "xyzzzzzzzzzzz")


if __name__ == "__main__":
    app.run(debug=False) 

