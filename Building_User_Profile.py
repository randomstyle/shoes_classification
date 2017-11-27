
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp
import pandas as pd


df = pd.read_csv('adult-test_titled.csv')
meta = pd.read_csv('meta-data-bin.csv')


# In[2]:


df.count()


# In[3]:


meta.count()


# In[4]:


df.describe()


# In[5]:


meta.describe()


# In[6]:


df.head(10)


# In[7]:


meta.head(10)


# In[8]:


len(meta.columns)
#too many columns we do not need all of them so we are going to select part of them as our features.


# In[9]:


df.axes


# In[10]:


meta.axes


# In[11]:


labels = meta.axes[1].tolist()
#turn the meta data file to our label list
labels.pop(0) # we don't want the first one "CID"
print(len(labels))


# In[12]:


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


# In[18]:


Gender


# In[23]:


#build user profiles 
#for user 2
customer_profile = np.zeros((len(df),36))
print (customer_profile[1])


# In[56]:


for i in range(len(Gender)): 
    print(str(i) + " " + Gender[i])


# In[57]:


for i in range(len(Category)): 
    print(str(i + len(Gender)) + " " + Category[i])


# In[58]:


for i in range(len(HeelHeight)): 
    print(str(i + len(Gender) + len(Category)) + " " + HeelHeight[i])


# In[60]:


for i in range(len(SubCategory)): 
    print(str(i + 15) + " " + SubCategory[i])


# In[67]:


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
        if int(df.iloc[i,0]) > 50:
            #'Loafers'
            customer_profile[i][20]=1
            # shoe Flats
            customer_profile[i][25]=1   
            #'Slipper.Heels'
            customer_profile[i][27]=1
            #'Slipper Boot'
            customer_profile[i][19]=1
            # Slipper.Flats
            customer_profile[i][21]=1
            # low heel height
            customer_profile[i][8]=1
            customer_profile[i][10]=1
            customer_profile[i][11]=1
        elif int(df.iloc[i,0]) >= 18: #age from 18 to 50
            #'Heels'
            customer_profile[i][28]=1   
            #sandal 'Heel'
            customer_profile[i][17]=1 
            #'Knee.High' 
            customer_profile[i][31]=1 
            # 'Ankle' 
            customer_profile[i][18]=1 
            # mid heel height
            customer_profile[i][9]=1            
            customer_profile[i][13]=1            
            if int(df.iloc[i,0]) <= 35:  #age from 18 to 35
                #'Over.the.Knee'
                customer_profile[i][35]=1
                #Flat sandals                 
                customer_profile[i][23]=1
                #Heel sandals                 
                customer_profile[i][17]=1
                #high heel height
                customer_profile[i][12]=1
                customer_profile[i][14]=1
            else:   #age from 35 to 50
                #24 Clogs.and.Mules
                customer_profile[i][24]=1
        elif int(df.iloc[i,0]) > 12:   #age from 12 to 18
             #Slipper.Flats
            customer_profile[i][21]=1  
            #'Sneakers.and.Athletic.Shoes'
            customer_profile[i][26]=1
            #flat sandals
            customer_profile[i][23]=1
            # low heel height
            customer_profile[i][8]=1
            customer_profile[i][10]=1
            customer_profile[i][11]=1
    elif "Male" in df.iloc[i,9]:
        customer_profile[i][0]=1 
         # very low heel height       
        customer_profile[i][10]=1
        customer_profile[i][11]=1
        #then shoes based on ages
        if int(df.iloc[i,0]) < 30:
            #'Sneakers.and.Athletic.Shoes'
            customer_profile[i][26]=1
            #29 Athletic sandals
            customer_profile[i][29]=1
        elif int(df.iloc[i,0]) < 40:
            #22 Boat.Shoes
            customer_profile[i][22]=1
            #20 Loafers
            customer_profile[i][20]=1
        elif int(df.iloc[i,0]) < 50:  
            #15 Oxfords
            customer_profile[i][15]=1
            #18 Ankle
            customer_profile[i][18]=1
        else:
            #'Slipper Boot'
            customer_profile[i][19]=1
            # Slipper.Flats
            customer_profile[i][21]=1
    #boys girls?
    #following is based on jobs
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



# In[68]:


customer_profile[11005]


# In[69]:


df.iloc[11005,:]  


# In[70]:


customer_profile[9888]


# In[71]:


df.iloc[9888,:]  


# In[ ]:




