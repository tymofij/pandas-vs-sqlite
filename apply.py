import pandas as pd


df = pd.read_csv('test.csv')
df['Fraud'] = df.apply(lambda row: df[
    (df.CustomerID==row['CustomerID']) & 
    (df.EventType==row['EventType']) & 
    (df.EventTime > row['EventTime'] - (4. / 24) ) & 
    (df.EventTime < row['EventTime'])
    ].size > 0, axis=1)

df.to_csv('output/apply.csv', columns=['EventID', 'Fraud'])
