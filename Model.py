# from joblib import dump, load
# import numpy as np
 

# def make_prediction(num):
#     model = load('filename.joblib')
#     X = np.array([[num]])
#     return model.predict(X)

###################################

from joblib import dump, load
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd

#Given the text, predict its classification
def make_prediction(text):
     model = load('nb.joblib')
     X = np.array([text])   #put text from webpage into an array object
     ### Nov 17
     # Y = remove_stop_words(X) #feature list
     clean_text = remove_stop_words(X)
     Y = np.array([clean_text]) #put text into array
     input_feature_list = get_feature_list(X)
     ##print("feature_list",get_feature_list(X))
     ###
     array = model.predict(Y)
     ##print(array)
     return array[0], input_feature_list;

#Remove stop words from a string
def remove_stop_words(text):
     vectorizer = TfidfVectorizer(stop_words='english')
     vectorizer.fit_transform(text)
     ### Nov 17
     text_array = vectorizer.get_feature_names()
     #print(text_array)
     clean_text = ' '.join(text_array)
     return clean_text
     # feature_list = vectorizer.get_feature_names()
     # return feature_list
     ###

#@input: an np.array ie: ['...','...','...']
#@return: a feature list
#@example: ['coding', 'experience', 'html', 'javascript', 'like', 'program', 'python', 'years']
def get_feature_list(text):
     vectorizer = TfidfVectorizer(stop_words='english')
     vectorizer.fit_transform(text)
     feature_list = vectorizer.get_feature_names()
     return feature_list

#@input: a list of arrays ie: [('...'),('...'),('...')]
#@return: a feature list, a weight list
#@example: ['coding', 'experience', 'html', 'javascript', 'like', 'program', 'python', 'years']
def get_corpus(x):
     df = pd.DataFrame(x)
     #print(df)
     X = df['job_description']
     vectorizer = TfidfVectorizer(stop_words='english')
     vec = vectorizer.fit_transform(X)
     corpus_feature_list =vectorizer.get_feature_names()
     #print("feature list",vectorizer.get_feature_names())
     #print("vec.shape",vec.shape)
     weights = np.zeros(vec.shape[1])
     #print(weights)
     array = vec.toarray()
     for a in array:
          weights = weights + a
     #print("weights",weights)
     print("weights.shape",weights.shape)
     return corpus_feature_list, weights;

def makeData(input, corpus, weights):
     chartData = []
     for i in range(len(corpus)):
          item = corpus[i]
          if item in input:
               chartData.append({"text": item, "weight": weights[i]*100})
     #print(chartData)
     return chartData
