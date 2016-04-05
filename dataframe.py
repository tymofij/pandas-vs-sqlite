import pandas as pd
df = pd.read_csv('test.csv')
# df = pd.read_csv('test1000.csv')

#df = df.set_index(['EventTime', 'CustomerID', 'EventType'], drop=False)
df = df.set_index('EventTime', drop=False)
df.sort_index(inplace=True)

df['Fraud'] = df.apply(lambda row: df[
    (df.CustomerID==row['CustomerID']) & 
    (df.EventType==row['EventType']) & 
    (df.EventTime > row['EventTime'] - (4. / 24) ) & 
    (df.EventTime < row['EventTime'])
    ].size > 0, axis=1)


del df['EventTime']
df.to_csv('d.csv')

dfx = df.copy()
dfx['Fraud'] = (
    dfx.groupby(['CustomerID', 'EventType'])
      .EventTime
      .transform(lambda group: group - group.shift())
      .lt(4. / 24))

del dfx['EventTime']
dfx.to_csv('x.csv')
