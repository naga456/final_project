# import necessary libraries
from flask import Flask, render_template,redirect,request
import Model, config

output = "Add your resume in the textbox and click submit"
final_prediction =""
data2 = []
myResults = [""]
chartdata = [{"text": "", "weight": 60}, {"text":"","weight":90}]
data3 = []

# create instance of Flask app
app = Flask(__name__)

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
url = "postgres://postgres:postgres@localhost/Jobs"

engine = create_engine(url)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Categories = Base.classes.categories


# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", text=output, chartdata = chartdata)

@app.route('/', methods=['POST','GET'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    output = processed_text
    prediction, input_feature_list = Model.make_prediction(output)
    session = Session(engine)
    myResults = session.query(Categories.job_description).filter(Categories.labels==prediction).limit(25).all()
    #myResults = session.query(Categories.job_description).filter(Categories.labels==prediction).all()
    corpus_feature_list, weights = Model.get_corpus(myResults) 
    chartdata = Model.makeData(input_feature_list,corpus_feature_list,weights)
    return render_template("index.html", text=prediction,myResults = myResults, chartdata=chartdata)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/technology")
def technology():
    return render_template('technology.html')

if __name__ == "__main__":
    app.run(debug=True)
