from joblib import dump, load
import numpy as np
 

def make_prediction(num):
    model = load('filename.joblib')
    X = np.array([[num]])
    return model.predict(X)
