#!/usr/bin/env python
# coding: utf-8

# In[1]:


docA = "bây giờ mận mới hỏi đào"
docB = "vườn hồng có lối ai vào hay chưa"


# In[2]:


wordsA = docA.split()
wordsB = docB.split()


# In[3]:


wordsA


# In[4]:


wordsB


# In[7]:


wordSet = set(wordsA).union(set(wordsB))


# In[8]:


wordSet


# In[9]:


wordDictA = dict.fromkeys(wordSet, 0) 
wordDictB = dict.fromkeys(wordSet, 0)


# In[10]:


wordDictA


# In[11]:


for word in wordsA:
    wordDictA[word]+=1
    
for word in wordsB:
    wordDictB[word]+=1


# In[12]:


wordDictA


# In[13]:


import pandas as pd
pd.DataFrame([wordDictA, wordDictB])


# In[14]:


def computeTF(wordDict, words):
    tfDict = {}
    wordsCount = len(words)
    for word, count in wordDict.items():
        tfDict[word] = count/float(wordsCount)
    return tfDict


# In[16]:


tfdocA = computeTF(wordDictA, wordsA)
tfdocB = computeTF(wordDictB, wordsB)


# In[17]:


tfdocA


# In[19]:


tfdocB


# In[20]:


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict


# In[21]:


idfs = computeIDF([wordDictA, wordDictB])


# In[22]:


idfs


# In[23]:


def computeTFIDF(tfDocs, idfs):
    tfidf = {}
    for word, val in tfDocs.items():
        tfidf[word] = val*idfs[word]
    return tfidf


# In[24]:


tfidfDocA = computeTFIDF(tfdocA, idfs)
tfidfDocB = computeTFIDF(tfdocB, idfs)


# In[25]:


import pandas as pd
pd.DataFrame([tfidfDocA, tfidfDocB])


# In[ ]:




