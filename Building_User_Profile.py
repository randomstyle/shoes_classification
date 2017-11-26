
# coding: utf-8

# In[8]:


import numpy as np
import scipy as sp
import pandas as pd


df = pd.read_csv('adult-test_titled.csv')
meta = pd.read_csv('meta-data-bin.csv')


# In[9]:


df.count()


# In[10]:


meta.count()


# In[11]:


df.describe()


# In[12]:


meta.describe()


# In[13]:


df.head(10)


# In[14]:


meta.head(10)


# In[15]:


len(meta.columns)
#too many columns we do not need all of them so we are going to select part of them as our features.


# In[16]:


df.axes


# In[17]:


meta.axes


# In[18]:


labels = meta.axes[1].tolist()
#turn the meta data file to our label list
labels.pop(0) # we don't want the first one "CID"
print(len(labels))


# In[19]:


SubCategory = list()
Category = list()
HeelHeight = list()
Closure = list()
Gender = list()
Material = list()
ToeStyle = list()
# we don't want the insole column
for label in labels:    
    shortLabel = label[label.find(".")+1:]   
    #print(shortLabel)
    if "SubCategory" in label:
       SubCategory.append(shortLabel)
    elif  "Category" in label:
       Category.append(shortLabel)
    elif  "HeelHeight" in label:
       HeelHeight.append(shortLabel)
    elif  "Closure" in label:
       Closure.append(shortLabel)
    elif  "Gender" in label:
       Gender.append(shortLabel)
    elif  "Material" in label:
       Material.append(shortLabel)
    elif  "ToeStyle" in label:
       ToeStyle.append(shortLabel) 


# In[37]:


len(SubCategory)


# In[21]:


ToeStyle


# In[22]:


Closure


# In[23]:


Category


# In[34]:


SubCategory


# In[33]:


Gender


# In[36]:


HeelHeight


# In[50]:


print(df.iloc[2,:])


# In[80]:


#build user profiles 
#for user 2
customer_profile = np.zeros((len(df),15))
print (customer_profile[1])


# In[81]:


len(df)


# In[91]:


for i in range(len(df)):
# Gender
    if "Female" in df.iloc[i,9]:
        customer_profile[i][1]=1
        if "Child" in df.iloc[i,7]:
            customer_profile[i][8]=1
            customer_profile[i][10]=1
            customer_profile[i][11]=1
        elif "Never-married" in df.iloc[i,5] or "Divorced" in df.iloc[i,5] or "Separated" in df.iloc[i,5]:
            customer_profile[i][9]=1
            customer_profile[i][12]=1
            customer_profile[i][13]=1
            customer_profile[i][14]=1
    elif "Male" in df.iloc[i,9]:
        customer_profile[i][0]=1          
    #boys girls?
    if "Machine" in df.iloc[i,6] or "Tech" in df.iloc[i,6] or "Prof" in df.iloc[i,6] or "Transport" in df.iloc[i,6] or "managerial" in df.iloc[i,6]:
        #Shoes
        customer_profile[i][4]=1
    if "fishing" in df.iloc[1,6] or "Armed" in df.iloc[i,6] or "cleaners" in df.iloc[i,6]:
        #Boots
        customer_profile[i][5]=1
    if "service" in df.iloc[i,6]: 
        #Sandals
        customer_profile[i][6]=1
    if "Craft" in df.iloc[i,6]:
        #Slippers
        customer_profile[i][7]=1



# In[92]:


customer_profile[11005]


# In[93]:


df.iloc[11005,:]  


# In[ ]:




