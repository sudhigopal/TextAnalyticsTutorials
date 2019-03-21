from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
 ]
# D = 4
countVec = CountVectorizer()
counts = countVec.fit_transform(corpus)
print(countVec.get_feature_names())
print(counts.toarray())

tfIdf = TfidfVectorizer()
frequency = tfIdf.fit_transform(corpus)
print(tfIdf.get_feature_names())

import pprint
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(frequency.toarray())

