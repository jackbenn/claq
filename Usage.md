
## Passed data

Basic data type:
First column: headers (noted by "!" ???)
Later columns: data

Grouped data:


refer to headers by column name (case sensitive, python-appropriate variable names)
Or by _0, _1, _2, etc


where "_1 > 18 and _2 == 1"
where "age > 18 and gender == 1"

sort -f state, age

aggr -f "state, mean(age)"

Maybe special functions that trigger aggregation???

Want to allow window functions...somehow?

group -f state, gender | select "mean(age)"

group state, gender
context state, gender
group -c state, gender

Are window functions like group by? Maybe no: there can be several contexts inside a select. So is the context specified in the select or the group statement?

select "state, mean(age):
select "state, age-mean(age)"

select "state, mean(age)|state"
select "state, age-mean(age)|state"

Maybe have a separate function for group by but not window?
Or with an option for window that just does tagging, e.g.

group -c "state" | select "state, age-mean(age)"
select "state, age-mean(age)|state"

do the same thing.

Aggregation functions
    No parameters
    count, order

    One parameter
    min, max, mean, median, stdev, var

    Two parameters
    percentile, cov

Functions
    exp, sin

