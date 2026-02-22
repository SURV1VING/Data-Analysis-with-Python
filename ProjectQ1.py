import numpy as np
import pandas as pd

data=pd.read_csv(r"C:\Users\Lulama\Downloads\Sethu's school file\ITAYA0\customers.csv")
#1a. display 5 rows

print("\n\n First 5 rows of the dataset:")
print(data.head(5)) #got this from an example sir made
print("\n\n Data structure:")
print(data.info())
print(data.describe())

#1b. find the mean and standard of deviation for age
age_column=data['age']   #Using boolean to identify customer under 25 got that from the ITAYA0 textbook
np.mean(age_column)
print("Mean age of customers:", np.mean(age_column))
np.std(age_column)
print("Standard deviation of customers age:", np.std(age_column))
#Panda boolean
mask=age_column<25
print(mask.value_counts(True))# i found this on google, pandas boolean is mask
# notes are also in textbook pg 99

#1c. using boolean indexing to filter data
booIndex=data[data['age']<25] #pg 97 from an example from Wes-McKinney-Python-for-Data-Analysis textbook
print(booIndex)

#1d.  Creating a new column

def age_group(age): #My brain power
    if age < 25:
        return ("Youth")
    elif 25 <= age < 60:
        return ("Adult")
    elif age > 60:
        return ("Senior")

data['age_group'] = data['age'].apply(age_group)  #google helped me make this happen
print("\n New data with age groups:")
print(data)
print(data['age_group'].value_counts()) #counts how much adults youths and seniors there are