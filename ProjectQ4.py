import sqlite3
import pandas as pd

#4a. Load Cleaned dataset into a SQLite database
data=pd.read_csv(r"C:\Users\Lulama\Downloads\Sethu's school file\ITAYA0\health_data (1).csv")
data.columns=data.columns.str.strip()
conn = sqlite3.connect("health_data.db")
#data.to_sql("health_data", conn, if_exists='replace', index=False)

#4b. Write a SQL query to count patients by sex and risk level.

query_risk_level_vs_sex = """     
SELECT sex, risk_level, COUNT(*) AS patient_count
FROM health_data
GROUP BY sex, risk_level;
ORDER BY sex, risk_level;
"""
result=pd.read_sql_query(query_risk_level_vs_sex, conn)
print(result.to_string(index=False))

#4c. Write a SQL query to calculate the average disease score per age group:

query_avg_disease_score = """
SELECT
    CASE
    WHEN age < 25 THEN 'YOUTH'
    WHEN age BETWEEN  25 AND 60 THEN 'ADULT'
    ELSE 'SENIOR'
     END AS age_group,
    AVG(disease_score) AS avg_disease_score
FROM patients
GROUP BY age_group;
"""
print(pd.read_sql_query(query_avg_disease_score, conn))


#4d.  Write a SQL query using CASE to classify patients as "Critical" or "Stable" and export the results to a CSV.
query_classify_patients = """
SELECT *,
    CASE
        WHEN disease_score > 90 OR blood_pressure > 140 THEN 'Critical'
        ELSE 'Stable'
    END AS patient_status
FROM health_data;   
"""
classified_data = pd.read_sql_query(query_classify_patients, conn)
classified_data.to_csv('classified_health_data.csv', index=False)
print("Classified data exported to 'classified_health_data.csv'")

#4e. explain how database indexes could improve query performance in large-scale health systems

'''
A Database index scan through columns, without having
to process the whole table making finding what you're looking for faster.
'''