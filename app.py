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

############
# from flask_sqlalchemy import SQLAlchemy
# url = "postgres://postgres:postgres@localhost/Jobs"
# app.config['SQLALCHEMY_DATABASE_URI'] = url
# db = SQLAlchemy(app)

# class Categories(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     label = db.Column(db.String(),unique=False)
#     job_description = db.Column(db.String(),unique=False)

############

###
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

# @NOTE: Set scrape
@app.route("/scrape")
def scraper():

    print("test button")

    # Redirect back to home page
    return redirect("/")

@app.route("/submit")
def submission():
    ###print("submit button")
    return redirect("/")

@app.route('/', methods=['POST','GET'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    #print(processed_text)
    output = processed_text
    #num = int(text)
    prediction, input_feature_list = Model.make_prediction(output)
    #final_prediction = prediction
    print("prediction",prediction)
    ###
    session = Session(engine)
    #myResults = session.query(Categories.job_description).filter(Categories.labels.in_("Marketing")).limit(5).all()
    #myResults = session.query(Categories.job_description).filter(Categories.labels=="Marketing").limit(5).all()
    #myResults = session.query(Categories.job_description).filter_by(**prediction).limit(5).all()
    myResults = session.query(Categories.job_description).filter(Categories.labels==prediction).limit(25).all()
    #myResults = session.query(Categories.job_description).filter(Categories.labels==prediction).all()
    #print(myResults)
    corpus_feature_list, weights = Model.get_corpus(myResults) 
    ###

    ### Nov 16
    data = [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 400.6]
    data2 = ["cat","the","hat","dog"]
    data3 = [{"text": "app.py", "weight": 60}, {"text":"data3","weight":90}]
    #data = "test data"
    ###

    ### Nov 17
    # prediction_feature_list = Model.get_feature_list(output)
    # print("prediction_feature_list",prediction_feature_list)
    chartdata = Model.makeData(input_feature_list,corpus_feature_list,weights)
    ###
    return render_template("index.html", text=prediction,myResults = myResults, chartdata=chartdata)


####
@app.route("/db")
def get_db():
    session = Session(engine)
    #myResults = session.query(Categories.labels).all()
    #myResults = "blank for now"
    #myResults = Categories.query.all()
    print(final_prediction)

    myResults = session.query(Categories.job_description).filter(Categories.labels.in_(final_prediction)).limit(5).all()
    return render_template('index.html', myResults = myResults)

####

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
