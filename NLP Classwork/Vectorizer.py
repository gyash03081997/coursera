#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

example="The cat was chasing a mouse"
example=[stemmer.stem(token) for token in example.split(" ")]


# In[3]:


print(" ".join(example))


# In[12]:


import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

example="The cat was chasing the mice"
example=[lemmatizer.lemmatize(token) for token in example.split(" ")]


# In[13]:


print(" ".join(example))


# In[11]:


print(lemmatizer.lemmatize('better',pos='a'))


# In[14]:


import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

example="The cat was chasing the mice. there were cacti round the corner"
example=[lemmatizer.lemmatize(token) for token in example.split(" ")]


# In[18]:


print(" ".join(example))


# In[19]:


from sklearn.feature_extraction.text import CountVectorizer


# In[24]:


vect=CountVectorizer(binary=True)#can explore other parameters like other than binary
corpus=["Tessaract is a good good optical recognition technique","optical character recognition is significant"]
vect.fit(corpus)
#print(vect.transform(["This is a good optical"]).toarray())
print(vect.transform(corpus).toarray())


# In[25]:


vect=CountVectorizer(binary=True)#can explore other parameters like other than binary
corpus=["Tessaract is a good good optical recognition technique","Tessaract is significant"]
vect.fit(corpus)
#print(vect.transform(["This is a good optical"]).toarray())
print(vect.transform(corpus).toarray())


# In[30]:


vocab=vect.vocabulary_ #vocabulary built in
for key in sorted(vocab.keys()):
    print("{}:{}".format(key,vocab[key]))


# In[ ]:





# In[ ]:





# In[ ]:




