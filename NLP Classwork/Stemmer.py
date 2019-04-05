#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download()


# In[2]:


from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


# In[3]:


porter=PorterStemmer()
lancaster=LancasterStemmer()
print("Porter Stemmer")
print(porter.stem("cats"))
print(porter.stem("trouble"))
print(porter.stem("troubling"))
print(porter.stem("troubled"))
print("Lancaster Stemmer")
print(lancaster.stem("cats"))
print(lancaster.stem("trouble"))
print(lancaster.stem("troubling"))
print(lancaster.stem("troubled"))


# In[4]:


print(lancaster.stem("apple"))
print(porter.stem("apple"))


# In[5]:


print(lancaster.stem("happiness"))
print(porter.stem("happiness"))


# In[6]:


print(lancaster.stem("Dying"))
print(porter.stem("Dying"))


# In[7]:


print(lancaster.stem("dying"))
print(porter.stem("dying"))


# In[8]:


print(lancaster.stem("impossible"))
print(porter.stem("impossible"))


# In[9]:


print(lancaster.stem("Impossible"))
print(porter.stem("Impossible"))


# In[10]:


print(lancaster.stem("prenuptial"))
print(porter.stem("prenuptial"))


# In[11]:


print(lancaster.stem("Prenuptial"))
print(porter.stem("Prenuptial"))


# In[12]:


print(lancaster.stem("Collage"))
print(porter.stem("Collage"))


# In[13]:


print(lancaster.stem("collage"))
print(porter.stem("collage"))


# In[14]:


print(lancaster.stem("distrustful"))
print(porter.stem("distrustful"))


# In[ ]:





# In[15]:


print(lancaster.stem("receive"))
print(porter.stem("receive"))
print(lancaster.stem("proctee"))
print(porter.stem("proctee"))


# In[16]:


print(lancaster.stem("Receive"))
print(porter.stem("Receive"))
print(lancaster.stem("Proctee"))
print(porter.stem("Proctee"))


# In[36]:


print(lancaster.stem("brownie"))
print(porter.stem("brownie"))


# In[18]:


print(lancaster.stem("employer"))
print(porter.stem("employer"))
print(lancaster.stem("employee"))
print(porter.stem("employee"))


# In[21]:


print(lancaster.stem("unhappy"))
print(porter.stem("unhappy"))
print(lancaster.stem("trilogy"))
print(porter.stem("trilogy"))


# In[22]:


print(lancaster.stem("collaborate"))
print(porter.stem("collaborate"))
print(lancaster.stem("corporate"))
print(porter.stem("corporate"))


# In[23]:


print(lancaster.stem("obliterate"))
print(porter.stem("obliterate"))
print(lancaster.stem("crate"))
print(porter.stem("crate"))


# In[24]:


print(lancaster.stem("obliterate"))
print(porter.stem("obliterate"))


# In[25]:


print(lancaster.stem("salutation"))
print(porter.stem("salutation"))
print(lancaster.stem("information"))
print(porter.stem("information"))
print(lancaster.stem("generation"))
print(porter.stem("generation"))
print(lancaster.stem("exclaimation"))
print(porter.stem("exclaimation"))
print(lancaster.stem("speculation"))
print(porter.stem("speculation"))
print(lancaster.stem("hibernation"))
print(porter.stem("hibernation"))
print(lancaster.stem("manipulation"))
print(porter.stem("manipulation"))
print(lancaster.stem("application"))
print(porter.stem("application"))
print(lancaster.stem("termination"))
print(porter.stem("termination"))
print(lancaster.stem("retribution"))
print(porter.stem("retribution"))
print(lancaster.stem("distribution"))
print(porter.stem("distribution"))
print(lancaster.stem("execution"))
print(porter.stem("execution"))
print(lancaster.stem("substitution"))
print(porter.stem("substitution"))
print(lancaster.stem("movement"))
print(porter.stem("movement"))
print(lancaster.stem("predicament"))
print(porter.stem("predicament"))
print(lancaster.stem("abolishment"))
print(porter.stem("abolishment"))
print(lancaster.stem("infringement"))
print(porter.stem("infringement"))
print(lancaster.stem("attainment"))
print(porter.stem("attainment"))
print(lancaster.stem("accomplishment"))
print(porter.stem("accomplishment"))


# In[26]:


print(lancaster.stem("incredible"))
print(porter.stem("incredible"))
print(lancaster.stem("invincible"))
print(porter.stem("invincible"))
print(lancaster.stem("forcible"))
print(porter.stem("forcible"))
print(lancaster.stem("visible"))
print(porter.stem("visible"))


# In[27]:


print(lancaster.stem("gillible"))
print(porter.stem("gullible"))
print(lancaster.stem("tangible"))
print(porter.stem("tangible"))
print(lancaster.stem("possible"))
print(porter.stem("possible"))
print(lancaster.stem("collapsible"))
print(porter.stem("collapsible"))
print(lancaster.stem("accessible"))
print(porter.stem("accessible"))
print(lancaster.stem("convertible"))
print(porter.stem("convertible"))
print(lancaster.stem("permissible"))
print(porter.stem("permissible"))


# In[31]:


print(lancaster.stem("abider"))
print(porter.stem("abider"))
print(lancaster.stem("abetter"))
print(porter.stem("abetter"))
print(lancaster.stem("abater"))
print(porter.stem("abater"))
print(lancaster.stem("adopter"))
print(porter.stem("adopter"))
print(lancaster.stem("adorner"))
print(porter.stem("adorner"))


# In[32]:


print(lancaster.stem("ionization"))
print(porter.stem("ionization"))
print(lancaster.stem("activization"))
print(porter.stem("activization"))
print(lancaster.stem("realization"))
print(porter.stem("realization"))


# In[33]:


print(lancaster.stem("acidified"))
print(porter.stem("acidified"))
print(lancaster.stem("allied"))
print(porter.stem("allied"))
print(lancaster.stem("amplified"))
print(porter.stem("amplified"))
print(lancaster.stem("beautified"))
print(porter.stem("beautified"))
print(lancaster.stem("identified"))
print(porter.stem("identified"))
print(lancaster.stem("buried"))
print(porter.stem("buried"))
print(lancaster.stem("humidified"))
print(porter.stem("humidified"))
print(lancaster.stem("abducted"))
print(porter.stem("abducted"))
print(lancaster.stem("aborted"))
print(porter.stem("aborted"))
print(lancaster.stem("abandoned"))
print(porter.stem("abandoned"))
print(lancaster.stem("accorded"))
print(porter.stem("accorded"))
print(lancaster.stem("aligned"))
print(porter.stem("aligned"))
print(lancaster.stem("alleged"))
print(porter.stem("alleged"))
print(lancaster.stem("curated"))
print(porter.stem("curated"))


# In[35]:


print(lancaster.stem("abhor"))
print(porter.stem("abhor"))
print(lancaster.stem("abjudicator"))
print(porter.stem("abjudicator"))
print(lancaster.stem("acceptor"))
print(porter.stem("acceptor"))
print(lancaster.stem("frown"))
print(porter.stem("circulator"))
print(lancaster.stem("circulator"))
print(porter.stem("commentor"))
print(lancaster.stem("commentor"))
print(porter.stem("corridor"))
print(lancaster.stem("corridor"))
print(porter.stem("corridor"))
print(lancaster.stem("decorator"))
print(porter.stem("decorator"))
print(lancaster.stem("exclaimator"))
print(porter.stem("exclaimator"))


# In[39]:


print(lancaster.stem("crying"))
print(porter.stem("crying"))
print(lancaster.stem("Dying"))
print(porter.stem("Dying"))
print(lancaster.stem("dying"))
print(porter.stem("dying"))


# In[ ]:




