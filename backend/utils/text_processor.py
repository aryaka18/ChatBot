from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import get_close_matches
import string
from .constants import KEYWORDS
# import nltk

class TextProcessor:
    def __init__(self):
        # nltk.download('punkt') 
        # nltk.download('stopwords')
        
        self.stop_words = set(stopwords.words('indonesian'))
        
        # Add word exception 
        self.exceptions = {"tugas", "akhir", "tugas akhir"} # antara 2 kata ini masuk kedalam stopwords indonesia, jadi harus ditambahkan exception

    def preprocess_text(self, text):
        for word in [exc for exc in self.exceptions if ' ' in exc]:
            if word in text.lower():
                text = text.lower().replace(word, word.replace(' ', '_'))
        
        # process individual words
        tokens = word_tokenize(text)
        tokens = [
            word.replace('_', ' ')  # Restore original words
            for word in tokens 
            if (word not in string.punctuation and 
                (word in self.exceptions or word not in self.stop_words))
        ]
        return tokens

    def auto_correct(self, word):
        possible_words = list(KEYWORDS.keys())
        matches = get_close_matches(word, possible_words, n=1, cutoff=0.7)
        return matches[0] if matches else word