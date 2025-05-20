#!/usr/bin/env python
# coding: utf-8

# # Dictionary
# ## Python Dictionaries
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# In[1]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)


# In[6]:


sr = {'name':'Samarth', 'age':22, 'Branch': 'AI'}
print(sr)


# ## Accessing Dictionary items:
# ### I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

# In[2]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))


# In[9]:


sr = {'name':'Samarth', 'age':22, 'Branch':'AI'}
print(sr['name'])


# In[11]:


print(sr.get('name'))


# ### II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

# In[3]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())


# In[12]:


sr = {'name': 'Samarth', 'Age':22, 'Branch':'AI'}
print(sr.keys())


# ### III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

# In[4]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())


# In[13]:


sr = {'Name': 'Samarth', 'Age': 22, 'Branch':'AI'}
print(sr.keys())


# ### IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

# In[5]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())


# In[15]:


sr = {'Name':'Samarth', 'Age': '20', 'Branch':'AI'}
print(info.items())


# In[ ]:




