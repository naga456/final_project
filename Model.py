from joblib import dump, load
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd

#Given the text, predict its classification
def make_prediction(text):
     model = load('nb.joblib')
     X = np.array([text])   #put text from webpage into an array object
     clean_text = remove_stop_words(X)
     Y = np.array([clean_text]) #put text into array
     input_feature_list = get_feature_list(X)
     array = model.predict(Y)
     return array[0], input_feature_list;

#Remove stop words from a string
def remove_stop_words(text):
     vectorizer = TfidfVectorizer(stop_words='english')
     vectorizer.fit_transform(text)
     text_array = vectorizer.get_feature_names()
     clean_text = ' '.join(text_array)
     return clean_text

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
     X = df['job_description']
     vectorizer = TfidfVectorizer(stop_words='english')
     vec = vectorizer.fit_transform(X)
     corpus_feature_list =vectorizer.get_feature_names()
     weights = np.zeros(vec.shape[1])
     array = vec.toarray()
     for a in array:
          weights = weights + a
     print("weights.shape",weights.shape)
     return corpus_feature_list, weights;

def makeData(input, corpus, weights):
     chartData = []
     for i in range(len(corpus)):
          item = corpus[i]
          if item in input:
               chartData.append({"text": item, "weight": weights[i]*100})
     return chartData
