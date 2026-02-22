import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.computation.ops import isnumeric

#3a Load dataset Identify missing values, outliers, and duplicates

Data=pd.read_csv(r"C:\Users\Lulama\Downloads\Sethu's school file\ITAYA0\health_data (1).csv")
Data.duplicated().value_counts() #Pandas website to count duplicates
print("There are", Data.duplicated().sum(), "duplicates rows in the dataset.")
Data.isna().sum()
print("There are", Data.isna().sum(), "missing values in the dataset.")
summary=Data.describe() #gettimg summary of the data
q1=summary.loc['25%'] #finding the quartiles to find IQR
q3=summary.loc['75%']
IQR=q3-q1     #Finding IQR to calculate outliers
lower_bound=q1-(1.5*IQR)
upper_bound=q3+(1.5*IQR)

BMI= Data['BMI'] #tried to get the data from each column
blood_pressure= Data['blood_pressure']
disease_score= Data['disease_score']

outlier_BMI = Data[(Data['BMI'] < lower_bound['BMI']) | (Data['BMI'] > upper_bound['BMI'])] # tried finding outliers for each column
outlier_blood_pressure = Data[(Data['blood_pressure'] < lower_bound['blood_pressure']) | (Data['blood_pressure'] > upper_bound['blood_pressure'])]
outlier_disease_score = Data[(Data['disease_score'] < lower_bound['disease_score']) | (Data['disease_score'] > upper_bound['disease_score'])]

print("The outlier of blood pressure is:", outlier_blood_pressure) #not the result i wanted will ask for help
print("The outlier of BMI is:", outlier_BMI)
print("The outlier of the disease score is:", outlier_disease_score)

#3b. ean the blood_pressure column using regular expressions to remove non-numeric characters and convert it to float.

import re   #pg 229 regular expressions
Data['blood_pressure'] = Data['blood_pressure'].astype(str).apply(lambda x: re.sub(r'[^0-9.]', '', x))
Data['blood_pressure'] = pd.to_numeric(Data['blood_pressure'], errors='coerce')
print(Data['blood_pressure'].head())

#3c.  Create a new column risk_level using a lambda function:

risk_level=[]
def short_function(BMI, disease_score): #RELEASE ME PLEASE pg70
 if BMI >30 and disease_score > 80:
     risk_level.append("High")
 elif BMI > 25 and disease_score > 60:
     risk_level.append("Medium")
 else:
     risk_level.append("Low")
Data.apply(lambda column: short_function(column['BMI'], column['disease_score']), axis=1)
Data['risk_level']=risk_level
print(Data)

#3d.
BMI.groupby(Data['risk_level']).mean()
print("The average BMI is:", BMI.groupby(Data['risk_level']).mean())
disease_score.groupby(Data['risk_level']).mean()
print("The average disease score is:", disease_score.groupby(Data['risk_level']).mean())

# 3e. create a box plot of BMI by risk_level and a histogram of age. Label axes and add titles.
'''
import matplotlib.pyplot as plt  
figAxis=plt.subplots(figSize=(10,10)) #example from mylms
XaxisHis=(Data['age'], bin = [0, 20, 40, 60, 80, 100])
YaxisHis=(BMI.groupby(Data['risk_level']).mean())
'''
Data=pd.DataFrame({"BMI": BMI, "risk_level": Data['risk_level'], "age": Data['age']})
ax=Data.boxplot(column='BMI', by='risk_level', grid=False)  #Panda website
plt.show()

Data=pd.DataFrame({"age": Data['age'], "BMI": BMI, "risk_level": Data['risk_level']})
Figure=Data['age'].plot.hist(bins=[0, 20, 40, 60, 80, 100], grid=False)
plt.xlabel("age")
plt.ylabel("BMI and risk level")
plt.show()