"""
Stop Words
"""

from nltk import download
from nltk.corpus import stopwords


download('stopwords')

stop_words=set(stopwords.words('english'))

print(type(stop_words), stop_words)
