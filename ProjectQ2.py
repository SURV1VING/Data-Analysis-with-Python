import pandas as pd
import matplotlib.pyplot as plt

#2a. Convert the subscription_date column to datetime format
data=pd.read_csv(r"C:\Users\Lulama\Downloads\Sethu's school file\ITAYA0\customers.csv")
print(data)

print("\nData in datetime format:")
data['subscription_date']=pd.to_datetime(data['subscription_date'], errors='coerce') #pg41... was useless # Pandaspydata.org my love
data['year_joined']=data['subscription_date'].dt.year  # free styled the rest
data['month_joined']=data['subscription_date'].dt.month
data['quarter_joined']=data['subscription_date'].dt.to_period('Q')
print("\n\nData with new time based column:")
print(data)

#2b. find average age group and subscription year for those age groups

data.groupby(data['age_group']).mean()
data.groupby(data['age'].mean())   # got this from pandas website
data.groupby(data['year_joined'].mean())
print(f"The average subscription_year:", {'data[year_joined].mean()'}, "The average age:", {data['age'].mean()})

#2c. bar graph of signups per year

'''
Number_of_signups = data["year_joined"].value_counts().sort_index()
plt.figure(figsize=(10,6))
Number_of_signups.plot(kind='bar', color="blue")
plt.title("Number of signups per year")
plt.xlabel("Years")
plt.ylabel("Number of signups")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''

data=pd.DataFrame({"year_joined": data['year_joined'], "yearly_signups": data['year_joined'].value_counts})
ax=data.plot.bar(x="year_joined", y="yearly_signup", rot=0)
plt.xlabel("year_joined")
plt.ylabel("Yearly_signups")
plt.title("Bar graph of signups per year")
plt.show()

#2d. pie chart of distribution of customers age groups

age_group_counts = data['age_group'].value_counts()
plt.figure(figsize=(6, 6))
age_group_counts.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Distribution of customers by age group")
plt.ylabel('')

#2e. save a cleaned dataset
data.to_csv('Customers_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'Customers_cleaned.csv'")





