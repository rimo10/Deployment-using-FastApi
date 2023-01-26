import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))


def predict(text):
    text = text.split(' ')
    text = [' '.join(text)]
    text = tfidf.transform(text)
    prob = model.predict(text)
    return prob
