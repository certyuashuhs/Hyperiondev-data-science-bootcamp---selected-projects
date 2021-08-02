import spacy

# Note: I have written my observations at the bottom of this file

nlp = spacy.load('en_core_web_md')
nlp2 = spacy.load('en')

#variables tokenized with core_web_md model
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# creating my own test of 3 different things
own1 = nlp("car")
own2 = nlp("boat")
own3 = nlp("garage")

#variables tokeized with 'en' model
word1_new = nlp2("cat")
word2_new = nlp2("monkey")
word3_new = nlp2("banana")

# doing comparison with core_web_md model on my own variables
print("My own comparison")
print(own1.similarity(own2))
print(own3.similarity(own2))
print(own3.similarity(own1))

print()
# comparison with core_web_md model 
print("comparisons via \'core_web_md\' model")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print()
# comparison with core_'en' model 
print("comparisons via \'en\'model")
print(word1_new.similarity(word2_new))
print(word3_new.similarity(word2_new))
print(word3_new.similarity(word1_new))

tokens = nlp('cat apple monkey banana ') # tokenizing with core_web_md model
tokens2 = nlp2('cat apple monkey banana ') # tokenizing with 'en' model

print()
# comparison with core_web_md model
print("comparisons via \'core_web_md\' model")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()
# comparison with 'en' model
print("comparisons via \'en\' model")
for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello, where is my car",
             "I\'ve lost my cat in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare) # tokenizing with core_web_md model
model_sentence_2 = nlp2(sentence_to_compare) # tokenizing with 'en' model

print()
print("comparing with \'core_web_md\' language model")

# comparison with core_web_md model
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f'sentence - {similarity}')

print()
print("comparing with \'en\' language model")

# comparison with 'en' model
for sentence in sentences:
    similarity = nlp2(sentence).similarity(model_sentence_2)
    print(f'sentence - {similarity}')
    '''
    Observations: with my own example the biggest similarity between car, boat and garage is car and garage.
    With cat, monkey, banana the biggest similarity is between monkey and banana (both models) with the 'en' model 
    showing higher correlation (probaly due to taking different factors into consideration).
    Overall the 'en' model tends to show higher correlation and similarity than the core_web_md model with singular words as in the first and second part.
    Where sentences were involved (part3), 'en'model showed lower correlation than the core_web_md model. This os probably due to web_md being better equipped at recognizing patterns where 
    sentences are involved.
    '''   
