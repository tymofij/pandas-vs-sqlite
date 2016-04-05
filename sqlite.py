import sqlite3, csv
import pandas as pd
from collections import namedtuple


db = sqlite3.connect(':memory:')
Event = namedtuple('Event', 'customer_id, event_id, event_type, event_time')

db.executescript('''
    CREATE TABLE events(
        customer_id int, 
        event_id int, 
        event_type text, 
        event_time real,
        fraud bool
    );
    CREATE INDEX customer_idx ON events(customer_id);
    CREATE INDEX event_type_idx ON events(event_type);
    CREATE INDEX event_time_idx ON events(event_time);    
''')
events = []

sql = "BEGIN;"
reader = csv.reader(open('test.csv', 'r'))
next(reader)
for e in map(Event._make, reader):
    sql += '''
        INSERT INTO events(customer_id, event_id, event_type, event_time)
        VALUES ({}, {}, "{}", {});'''.format(*e)
    events.append(e)
sql += "COMMIT;"
db.executescript(sql)

cur = db.cursor()
for k, e in enumerate(events):
    cur.execute('''
        SELECT count(*) from events 
        WHERE customer_id=:customer_id 
            AND event_type=:event_type
            AND (event_time BETWEEN :past_4_hours AND :event_time)
        ''', {
            'customer_id': e.customer_id, 
            'event_type': e.event_type,
            'past_4_hours': (float(e.event_time)-(4./24)),
            'event_time': e.event_time,
            }
    )
    n, = cur.fetchone()
    fraud = n > 1 # meaning some other event besides this one happened in the past four hours
    events[k] = list(e) + [fraud]

df = pd.DataFrame(events, columns=['CustomerID', 'EventID', 'EventType', 'EventTime', 'Fraud'])

df.to_csv('output/sqlite.csv', columns=['EventID', 'Fraud'])