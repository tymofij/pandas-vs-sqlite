import pandas as pd


df = pd.read_csv('test.csv').sort_values('EventTime')
df['Fraud'] = df.groupby(['CustomerID', 'EventType']
    ).EventTime.transform(lambda group: group - group.shift()).lt(4. / 24)
df.sort_values('EventID', inplace=True)

df.to_csv('output/group.csv', columns=['EventID', 'Fraud'])
