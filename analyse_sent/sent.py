import os
import random
import spacy
from spacy.util import minibatch, compounding
import pandas as pd
nlp = spacy.load("en_core_web_sm")
data = pd.read_csv("emily1.csv")
text = []
for line in data.Line:
    text.append(clean_text(line))

    text_spacy = nlp(data['Line'])
    data['Line'].apply(nlp)
    document = nlp(text.decode())
