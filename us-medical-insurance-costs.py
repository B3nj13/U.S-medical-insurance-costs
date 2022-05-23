#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[1]:


import csv
with open('insurance.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))


# In[95]:


import csv
rows = []
with open("insurance.csv", 'r')as file: 
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(type(rows))


# In[94]:


import pandas as pd
data = pd.read_csv("insurance.csv")
data_df = pd.DataFrame(data, columns=['age', 'sex', 'bmi', 'children','smoker','region','charges'])
#turned data into data Frames for easier processing in pandas into lists
#print(data_df)
county = 0
countno = 0
#setting data into lists to parse through for conditions
list_fam = data_df['children'].to_list()
list_smoker = data_df['smoker'].to_list()
list_region = data_df['region'].to_list()
list_charges = data_df['charges'].to_list()

#combinig lists for target data insight "smokers with families, region N or S" 
Adults = list(zip(list_fam,list_smoker,list_region))
#print(Adults)
for smokes in list_smoker:
    if smokes == 'yes':
        county += 1
    else:
        countno += 1
print(str(county/(county + countno)*100)+"% of the sample population are smokers")
countp = 0
for adult in Adults:
    print(adult)
    for z in adult:
        if z == 'northwest'or z == 'northeast':
            print((z))
            countp += 1 
        
print(str(countp)+" out of "+str(county + countno)+" is how much of the sample population are from the Northern region")


# In[ ]:



    


# In[133]:


import numpy as np
df = pd.read_csv('insurance.csv', usecols=['age', 'sex', 'bmi', 'children','smoker','region','charges'])


#population from northern region who smoke and have family

pnw = df[(df.children > 0) & (df.smoker == 'yes')&(df.region == 'northeast')]
pne = df[(df.children > 0) & (df.smoker == 'yes')&(df.region == 'northwest')]
print(pnw)
#population from southern region who smoke and have family

psw = df[(df.children > 0) & (df.smoker == 'yes')&(df.region == 'southeast')]
pse = df[(df.children > 0) & (df.smoker == 'yes')&(df.region == 'southwest')]
print(pnw.charges)

#Want to know average costs of both groups in order to compare costs and conditions
#first change charges data frames into Numpy arrays easier mathematical augmentation
pnwc = pnw.charges.to_numpy()
pnec = pne.charges.to_numpy()
psec = pse.charges.to_numpy()
pswc = psw.charges.to_numpy()
avgpnw = np.average(pnwc)
avgpne = np.average(pnec)
avgpsw = np.average(pswc)
avgpse = np.average(psec)
#print averages as rounded numbers so as to give baseline of costs
print("The average cost for smokers with children in the Northwest is $"+str(np.round(avgpnw,2)))
print("The average cost for smokers with children in the Northeast is $"+str(np.round(avgpne,2)))
print("The average cost for smokers with children in the Southwest is $"+str(np.round(avgpsw,2)))
print("The average cost for smokers with children in the Southeast is $"+str(np.round(avgpse,2)))
#describe() shows a quick statistic summary of your data ex:
print(pnw.describe())
print(pne.describe())


# In[ ]:




