#Enable open source modules to enable certain libraries and excuse any restrictions
import pandas as pd

from matplotlib import pyplot as plt

import numpy as np

#Import the data that is saved under the created folder
data = pd.read_csv('tips.csv', index_col=0)
print(data)


#Create a new column that has a calculation
data["discount"] = data["tip"]/data["size"] 

data

#Refine the data by creating a subset based on conditions for females
cb = data[data.time == "Dinner"]
cb2 = cb[cb.smoker == "Yes"]
cb3 = cb2[cb2.sex == "Female"]

#Create a subset based on the conditions made for males
ca2 = cb[cb.smoker == "Yes" ]
ca3 = ca2[ca2.sex == "Male"]





#Create a graph to illustrate the findings
plt.plot(ca3.sex, ca3.discount)
plt.plot(cb3.sex, cb3.discount)
#Create Title
plt.title('Gender Tipping Rates', color= 'red', fontsize = 'x-large')
#Create Legend
plt.legend(['Males','Females'], fontsize = 'large')
#Create the axis labels
plt.xlabel('Gender', fontsize = 'x-large')
plt.ylabel('Tip rate per number of customers on a table', fontsize = 'x-large')
#Show the graph
plt.show()





