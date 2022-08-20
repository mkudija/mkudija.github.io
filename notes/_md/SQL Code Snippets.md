---
publish: true
---
# SQL Code Snippets

### Search for Column Names
```sql
SELECT *  
FROM INFORMATION_SCHEMA.COLUMNS  
WHERE COLUMN_NAME LIKE '%search%'  
ORDER BY TABLE_NAME;
```

### Joins
`on`
```SQL
FROM information_schema.tables t
	JOIN information_schema.columns c 
           on c.table_name = t.table_name 
           and c.table_schema = t.table_schema
```

`using`
```SQL
FROM information_schema.tables t
	JOIN information_schema.columns c USING(table_name, table_schema)
```


### Find tables with `colName` column

```SQL
select t.table_schema,
       t.table_name
from information_schema.tables t
inner join information_schema.columns c 
           on c.table_name = t.table_name 
           and c.table_schema = t.table_schema
where c.column_name = 'colName'
      and t.table_schema not in ('information_schema', 'pg_catalog')
      and t.table_type = 'BASE TABLE'
order by t.table_schema;
```


### Unique items in **`column`**

```SQL
SELECT 
    t.device
FROM 
    database.table t
GROUP BY t.device
```

|   | device       |
|---|--------------|
| 1 | "iPhone10,1" |
| 2 | "iPhone10,2" |
| 3 | "iPhone10,3" |
| 4 | "iPhone10,4" |
| 5 | "iPhone10,5" |


### value_count of **`column`**

```SQL
SELECT 
    value_count_col
    ,COUNT(id_col) AS value_count
FROM 
    database.table t
GROUP BY 1
ORDER BY 2 DESC
```

```SQL
SELECT 
    t.device
    ,COUNT(t.distance) AS value_count
FROM 
    database.table t
GROUP BY t.device
ORDER BY value_count DESC
```

|   | device     | value_count |
|---|------------|-------|
| 1 | iPhone10,5 | 23832 |
| 2 | iPhone10,2 | 14553 |
| 3 | iPhone10,4 | 3487  |
| 4 | iPhone10,3 | 3078  |
| 5 | iPhone10,1 | 23    |


### `np.where` equivalent for cases

```SQL
CASE
    WHEN t.score BETWEEN 0  AND 24  THEN '0-24'
    WHEN t.score BETWEEN 25 AND 49  THEN '25-49'
    WHEN t.score BETWEEN 50 AND 74  THEN '50-74'
    WHEN t.score BETWEEN 75 AND 100 THEN '75-100'
    ELSE 'OTHER'
END AS score_group
```


### Select only first/last record using `RANK() OVER PARTITION BY`

In this example, there may be many records for a given `user_id`, but we only want to select the most recent record for each `user_id`. Alternatively, we could select the first record by using `ASC`:

```SQL
SELECT
    ...
    ...
    FROM(
    SELECT
        ...
	...
        ,RANK() OVER (PARTITION BY t.user_id ORDER BY t.created_at DESC) AS RANK
        FROM
            database.table AS t
    )
WHERE RANK = 1
```

### Cumulative Value `SUM() OVER PARTITION BY`
In this value, LTV is a monthly value that we want to show cumulative amount:

```SQL
SELECT
    ...
    , SUM(ltv_prod)  
      OVER (PARTITION BY policy_effective_month  
      ORDER BY calendar_month ASC ROWS UNBOUNDED PRECEDING) AS ltv_cumulative
    FROM
            database.table AS t
    )
WHERE RANK = 1
```

### Round

`ROUND` rounds the number, and if you don't want the additional `.000` you can `CAST` as an integer:

`CAST(ROUND(col_name, 0) AS INT) AS col_name_rounded`

### Decile

Try the `NTILE` function ([link](https://www.geeksforgeeks.org/ntile-function-in-sql-server/)).

To get actual deciles you can use a `CASE` statement:
```SQL
SELECT 
    score_decile, 
    COUNT(score_decile) AS count
FROM (
    SELECT
        *,
        CASE
            WHEN score < 10 THEN '0-9'
            WHEN score > 9 AND score < 20 THEN '10-19'
            WHEN score > 19 AND score < 30 THEN '20-29'
            WHEN score > 29 AND score < 40 THEN '30-39'
            WHEN score > 39 AND score < 50 THEN '40-49'
            WHEN score > 49 AND score < 60 THEN '50-59'
            WHEN score > 59 AND score < 70 THEN '60-69'
            WHEN score > 69 AND score < 80 THEN '70-79'
            WHEN score > 79 AND score < 90 THEN '80-89'
            WHEN score > 89 THEN '90-100'
        END as score_decile
    FROM database.table
)
GROUP BY score_decile
ORDER BY score_decile
```

A quick trick is to `ROUND` with `-1` to approximate deciles if score is in the range from 0-100. This is not exact as your buckets will be `0-5`, `6-15`...`86-95`, `96-100` so the first and last buckets will be small, but if you are just comparing between two distributions and care less about the absolute distribution, this may be an easy trick.

```SQL
SELECT 
    score_decile_approx, 
    COUNT(score_decile_approx) AS count
FROM (
    SELECT
        *,
        ROUND(score, -1) AS score_decile_approx
    FROM database.table
)
GROUP BY score_decile_approx
ORDER BY score_decile_approx
```

Finally, we may want the *rate* rather than the count, which we can get with the `RATIO_TO_REPORT(count) OVER () AS rate` command. This gives `rate` for each row as a fraction of the sum of count `count` column.

```SQL
SELECT 
    score_decile_approx, 
    COUNT(score_decile_approx) AS count,
    RATIO_TO_REPORT(count) OVER () AS rate
FROM (
    SELECT
        *,
        ROUND(unmapped_score, -1) AS score_decile_approx
    FROM database.table

)
GROUP BY score_decile_approx
ORDER BY score_decile_approx
```

### Ratio over groupby

Above we use the `RATIO_TO_REPORT` command to get a ratio rather than count. If we want a time series showing percent, and it is groupe by time (week, month, etc.), this is how you get a rate for each group rather than the whole table:

```SQL
    RATIO_TO_REPORT(account_count) OVER(PARTITION BY DATE_TRUNC('month', account_timestamp))
```
or

```SQL
    DATE_TRUNC('quarter', account_timestamp) AS x,
    RATIO_TO_REPORT(account_count) OVER(PARTITION BY x)
```

### Number of items and most recent in table

```SQL
SELECT 
    COUNT(*), 
    MAX(created_at) 
FROM 
    database.table
```

### Rolling Mean

```SQL
SELECT 
    DATE_TRUNC('day', profile_timestamp) AS x,
    COUNT(DISTINCT account_id) AS new_user_count,
    AVG(new_user_count) OVER (ORDER BY x ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS count_rolling
FROM 
    database.table
```

### Percent Change
Display the `%` symbol:

```SQL
    CONCAT(ROUND((edw_PLE_months_30_4 - edw_PLE_months_30) / edw_PLE_months_30 * 100, 2),'\%') AS percent_diff
```

### Percent of Total
```SQL
earned_premium/SUM(earned_premium) OVER () as percent_of_total
```

or

```SQL
RATIO_TO_REPORT(earned_premium) OVER () AS percent_of_total
```

### Optimize Query
If you run the query with `EXPLAIN` on top it will give you the query plan and how costly each step is.

### Pivot Table
You can pivot, but you need to manually specify the column values:
```SQL
WITH pre AS (  
    SELECT state  
         , amount  
         , month  
    FROM state_mgt.planned_rate  
)  
SELECT *  
FROM pre PIVOT(SUM(amount) FOR MONTH IN ('2022-02-28','2022-03-30','2022-04-30'));
```

### Most Recent Month-End Date
```SQL
SELECT DATEADD(DAY, -1, DATE_TRUNC('month', CURRENT_DATE - 1)) AS most_recent_month_end_date
```


### Create & Update Tables
Create schema:
```SQL
-- create schema
CREATE SCHEMA my_schema;
```


Create table:
```SQL
-- create table
DROP TABLE IF EXISTS schema.table;
CREATE TABLE schema.table
	AS (
		SELECT * FROM table
	);
```

Update table:
```SQL
DELETE
FROM table
WHERE source = 'a';

INSERT INTO table
SELECT * FROM source_table
```

Grant usage:
```SQL
GRANT USAGE ON SCHEMA <name> TO user;
GRANT SELECT ON ALL TABLES IN SCHEMA <name TO user;

GRANT USAGE ON SCHEMA <name> TO GROUP readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA <name> TO GROUP readonly;
```

```SQL
GRANT USAGE ON [schema] TO mode_analytics;
GRANT SELECT ON [schema.table] TO mode_analytics;
```


### View Tables in Schema
```SQL
-- view tables in schema
SELECT t.table_name
FROM information_schema.tables t
WHERE t.table_schema = 'schema' -- put schema name here
	AND t.table_type = 'BASE TABLE'
ORDER BY t.table_name;
```

### Lag (Offset column by n rows)

```sql
SELECT
	col
	LAG(col, 1) OVER (ORDER BY calendar_month ASC) AS col_lag_7
```

### Development Months and Terms
`dev_mo` starts at 0, `term` starts at 1:

```sql
, DATEDIFF('month', policy_effective_month, calendar_month) AS dev_month  
, dev_month / 6 + 1 AS term
```

## Dates
### Last 7 days of data

```SQL
SELECT 
    *
FROM 
    database.table t
WHERE
    t.created_at > GETDATE() - INTERVAL '7 days'
```

### DATE_DIFF
```SQL
DATE_DIFF('month', start_month, calendar_month) AS age
```


### DATE_TRUNC

To transform a timestamp into weekly or daily etc. data use `DATE_TRUNC()`. Available `datepart`s are listed [here](http://www.postgresqltutorial.com/postgresql-date_trunc/).

```SQL
SELECT
    DATE_TRUNC('day', timestamp) AS day
```
or 
```SQL
SELECT
    DATE_TRUNC('week', timestamp) AS week
```
or
```SQL
SELECT
    DATE_TRUNC('month', timestamp) AS month
```
or
```SQL
SELECT
    DATE_TRUNC('quarter', timestamp) AS quarter
```

### Get month offset from current date (also end of month)
- `CURRENT_DATE` to get current date
- `DATEADD` to offset by a number of months
- `LAST_DAY` to get last day of month

```SQL
policy_inception_month = LAST_DAY(DATEADD(MM,-6, CURRENT_DATE))
```

*or*

```SQL
WHERE prediction_date = LAST_DAY(DATE_ADD('month', -1, CURRENT_DATE))
```

### Current Date

```sql
SELECT LEFT(GETDATE(),10)
```

## Resources
- [SQLBolt - Learn SQL](https://sqlbolt.com/)
- [SQLZOO](https://sqlzoo.net/wiki/SQL_Tutorial)
- [SQL Query Order of Execution](https://www.sisense.com/blog/sql-query-order-of-operations/)
- [Database Design for Mere Mortals](https://www.pearson.com/store/p/database-design-for-mere-mortals-25th-anniversary-edition/P100002994160/9780136788041)
- [The SQL Murder Mystery](https://mystery.knightlab.com/)

---
Created: [[2019-06-25-Tue]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
