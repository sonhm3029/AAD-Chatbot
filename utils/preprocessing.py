import nltk
import underthesea
from gensim.parsing.preprocessing import remove_stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

import re

def read_stopwords(filepath):
    lines = []

    # Open the file for reading
    with open(filepath, 'r', encoding='utf-8') as file:
        # Read each line in the file
        for line in file:
            # Append each line to the list, removing leading and trailing whitespace
            lines.append(line.strip())
            
    return lines

class Vi_Preprocessing:
    def __init__(self, txt):
        nltk.download["punkt"]
        
        # Sentence tokenize
        tokens = underthesea.sent_tokenize(txt)
        self.tokens = tokens
        self.tfidfvectorizer = TfidfVectorizer()
    
    
    def clean_sentence(self, sentence, stopwords=False):
        """Data learning
        - remove extra spaces, lowercase
        - remove unallowed word, symbol
        - remove stopwords
        """
        sentence = sentence.lower().strip()
        sentence = re.sub(r'[^a-zA-Z0-9\sÀÁẢẠÃĂẰẮẲẶẴÂẦẤẨẬẪÈÉẺẸẼÊỀẾỂỆỄÌÍỈỊĨÒÓỎỌÕÔỒỐỔỘỖƠỜỚỞỢỠÙÚỦỤŨƯỪỨỬỰỮỲÝỶỴỸàáảạãăằắẳặẵâầấẩậẫèéẻẹẽêềếểệễìíỉịĩòóỏọõôồốổộỗơờớởợỡùúủụũưừứửựữỳýỷỵỹđ]+', '', sentence)
        if stopwords:
            sentence = remove_stopwords(sentence)
        return sentence
    
    def get_cleaned_sentences(self, tokens, stopwords=False):
        cleaned_sentences = []
        for line in tokens:
            cleaned = self.clean_sentence(line, stopwords)
            cleaned_sentences.append(cleaned)
            
        return cleaned_sentences
    
    def cleanall(self):
        cleaned_sentences = self.get_cleaned_sentences(self.tokens, stopwords=True)
        cleaned_sentences_with_stopwords = self.get_cleaned_sentences(self.tokens, stopwords=False)
        
        return cleaned_sentences, cleaned_sentences_with_stopwords
    
    def TFIDF(self, cleaned_sentences):
        self.tfidfvectorizer.fit(cleaned_sentences)
        tfidf_vectors = self.tfidfvectorizer.transform(cleaned_sentences)
        self.tfidf_vectors = tfidf_vectors
        
        return tfidf_vectors
    
    def TFIDF_Q(self, question_to_be_cleaned):
        tfidf_vectors = self.tfidfvectorizer.transform([question_to_be_cleaned])
        return tfidf_vectors
    
    
    def doall(self):
        cleaned_sentences, cleaned_sentences_with_stopwords = self.cleanall()
        tfidf = self.TFIDF(cleaned_sentences)
        return [cleaned_sentences,cleaned_sentences_with_stopwords,tfidf]