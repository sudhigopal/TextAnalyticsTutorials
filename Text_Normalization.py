import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

sentence = "Hello how are you doing? I am done with the examples for this class"

ps = PorterStemmer()
_words = word_tokenize(sentence)
for word in _words:
    print(word,ps.stem(word))
lemma = WordNetLemmatizer()

_words = word_tokenize(sentence)
for word in _words:
    print(word,lemma.lemmatize(word))

stopword = set(stopwords.words('english'))
sentence = "If the Easter Bunny and the Tooth Fairy had babies would they take your teeth and leave chocolate for you?"
_words = word_tokenize(sentence)

filtered_sentence = [w for w in _words if w not in stopword]

print(filtered_sentence)