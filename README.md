Mark some records in dataset
============================ 

[Stackoverflow question](http://stackoverflow.com/questions/36381847/how-to-create-a-loop-or-function-for-the-logic-for-this-list-of-lists/36381930)

 The data set looks like this:

    CustomerID  EventID EventType   EventTime
    6           1        Facebook    42373.31586
    6           2        Facebook    42373.316
    6           3        Web         42374.32921
    6           4        Twitter     42377.14913
    6           5        Facebook    42377.40598
    6           6        Web         42378.31245

* `CustomerID`: the unique identifier associated with the particular customer
* `EventID`: a unique identifier about a particular online activity
* `EventType`: the type of online activity associated with this record (Web, Facebook, or Twitter)
* `EventTime`: the date and time at which this online activity took place. This value is measured as the number of days since January 1, 1900, with fractions indicating particular times of day. So for example, an event taking place at the stroke of midnight on January 1, 2016 would be have an EventTime of 42370.00 while an event taking place at noon on January 1, 2016 would have an EventTime of 42370.50.

What I need to do next is sort each record into the fraud or legit list of lists. A record would be considered fraudulent under the following parameters. As such, that record would go to the fraud list.

Logic to assign a row to the fraud list: The CustomerID performs the same EventType within the last 4 hours.

For example, row 2 (event 2) in the sample data set above, would be moved to the fraud list because event 1 happened within the last 4 hours. On the other hand, event 4 would go to the legit list because in there are no Twitter records that happened in the last 4 hours.

The data set is in chronological order.
