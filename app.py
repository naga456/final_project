# import necessary libraries
from flask import Flask, render_template,redirect,request
import Model

output = "Serving up cool text from the Flask server!!"
# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", text=output)

# @NOTE: Set scrape
@app.route("/scrape")
def scraper():

    print("test button")

    # Redirect back to home page
    return redirect("/")

@app.route("/submit")
def submission():
    print("submit button")
    return redirect("/")

@app.route('/', methods=['POST','GET'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    output = processed_text
    num = int(text)
    prediction = Model.make_prediction(num)
    return render_template("index.html", text=prediction)

if __name__ == "__main__":
    app.run(debug=True)
