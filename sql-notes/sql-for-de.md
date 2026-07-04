# 𝗦𝗤𝗟 𝗳𝗼𝗿 𝗗𝗮𝘁𝗮 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴
- [Youtube Link: Data Engineer Bootcamp](https://www.youtube.com/watch?v=ol9_NnC9-cc)
- Contents:

1. Setup & Basics
2. Operators & Functions
3. Terminal Intro
4. Local DuckDB Intro
5. VS Code Intro
6. Data Modeling & JOINs
7. Data Types
8. DDL & DML
9. Subqueries & CTEs
10. Data Modeling Pt.2
11. Functions (Date, Text, & NULL)
12. Window Functions
13. Nested Functions

<br>

## 1. Setup & Basics

### Database Hierarchy

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_22-44.png)

### Attaching a new database
- Go to your 'Notebooks' and select a notebook (example: 1.1 SQL & Database Setup)
- Click `+ Add Cell`
- Use the `ATTACH` command. Example: `ATTACH 'md:_share/data_jobs/a94f9b8a-2b8a-473f-bb86-de09552f052d' AS data_jobs;`
- Click `Run Cell` or press `ctrl + Enter`

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-00.png)

- **Diagram**
    - **Main fact table** - the job postings fact table
    - **Dimension table** - the other 3 tables

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-06.png)

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-17.png)

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-19.png)

<br>

### Basic Keywords
![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-24.png)

#### SELECT * / FROM

- **Select everything**
    - The asterisk means everything.
    - So this means we want to SELECT all the columns (everything) FROM job_postings_fact table

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-27.png)

- **Select specific columns**

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-38.png)

#### LIMIT
- limits the number of rows that will be shown
- better to put this on the bottom of your query
- better to end every query by a **semi-colon**

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-52.png)

#### DISTINCT
- Let's say we have the scenario where we want to look at **distinct values or unique values inside of a column**
- Example: Look at the 'job_title_short' column

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-48.png)

- We can get the distinct or unique keywords:

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-49.png)

#### WHERE
- To get specific value.
- In this example, we want to get specific job titles

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-54.png)

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-03_23-55.png)

- Note: No need to put quotes if you're filtering number types. But put **quotes** if your filtering text types, in this example, 'Data Engineer' 

#### NULL / IS NOT NULL
- If you want to filter **NULL** values, DON't use the `=` sign, but use `IS`. Example:

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-05.png)

- Obviously, if you want to filter and see everything that has values, use `IS NOT NULL`

#### Commenting Code

- `--` - used for single line comment

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-13_1.png)

- `/*` `*/` - used for multi line comment

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-15.png)

#### ORDER BY
- we can sort a column using this command

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-16.png)

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-17.png)

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-18.png)

#### Order of Commands

![alt text](images/sql-for-de/01-setup-and-basics/2026-07-04_00-19.png)

<br>
<br>
<br>

## 2. Operators & Functions

### Where are operators used?

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_12-37.png)

### Comparison Operators

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_12-25.png)

#### `=`
- Example: Show the jobs that are work from home.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_12-55.png)

#### `!=` or `<>`
- Example: Show all the jobs schedule type except for the 'Contractor'.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-04.png)

#### `>` `<` / `>=` `<=`
- Example: Show the salary year average that are greater than 100,000.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-08.png)

#### `BETWEEN`
- Example: Show the salary average between 100_000 and 200_000. 
- Note: You can use underscore `_` to separate the zeros.
- Note: 100_000 and 200_000 are included if you use `BETWEEN`

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-42.png)

- This can be written with `>=` and `<=` but it is less readable so we usually use `BETWEEN`

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-46.png)

#### `IN`
- Instead of using a lot of `OR`, we can use `IN` instead.
- Example: Show jobs that are 'Data Analyst' or 'Data Engineer' or 'Senior Data Engineer'

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-58.png)

#### Example (Putting it all together)
- Problem:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_14-03.png)

- Solution:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_14-08.png)

#### `LIKE` with wildcards `_` or `%`

##### Underscore`_` wildcard

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_14-18.png)

- Example: Show job locations in Columbus, and on any of its state. Since the data has 2 characters provided for the state, put 2 underscores `_ _` to match

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_14-55.png)

##### Percentage `%` wildcard

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_15-00.png)

- Example: Show jobs that have the 'Data Analyst' in it.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_15-05.png)

#### ALIAS `AS`
- To change a name of a column, or the name of the table.
- Example: Change the column name 'job_title' to 'job_title_original'

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_15-10.png)

#### Example (putting it all together)
- Problem:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_15-15.png)

- Solution:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_15-30.png)

<br>

### Logical Operators

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_12-35.png)

#### `AND`
- Example: Show 'Data Engineer' jobs that are work from home.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-24.png)

#### `OR`
- Example: Show 'Data Engineer' jobs or 'Senior Data Engineer' jobs.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-31.png)

#### `NOT`
- Example: Show the jobs that are not work from home. We can put `NOT` instead of putting `FALSE`.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-36.png)

- Example: Use **parenthesis** if you want to use `NOT` on both conditions.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_13-38.png)

<br>

### Arithmetic Operators

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_20-30.png)

#### Where else can we use these operators?

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_20-38.png)

#### Addition & Subtraction
- Example:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_20-55.png)

#### Multiplication
- Example:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_21-07.png)

#### Division
- Example:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_21-09.png)

#### Modulus
- Example: Filter out all the values that are not ending with 3 zeros.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_21-25.png)

<br>

### Aggregate Functions

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_21-35.png)

#### Used in conjunction with `GROUP BY` and/or `HAVING`
- `GROUP BY` allows you to segment by a certain condition. 
- `HAVING` allows you to filter.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-02.png)

#### COUNT()
- `COUNT(*)` Example:

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-38.png)

- Example: Show the number of rows for 'Data Engineer'.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-40.png)

- Example: If we wanted to find out what data engineer jobs have a yearly salary listed.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-47.png)

#### COUNT(DISTINCT)
- Example: Show the number of rows with unique job title (short).

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-51.png)

#### SUM()
- Example: Show the average salary.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-56.png)

#### AVG()
- Example: We can get the same result from the previous example by using `AVG()`

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_22-59.png)

#### GROUP BY
![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_23-00.png)

- Example: Show the average salary grouped by country, and sort it from highest to lowest.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_23-16.png)

#### MIN() / MAX()
- Example: Show the minimum and maximum value for each average value.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_23-23.png)

#### MEDIAN()
- Example: Get the middle value (median) for each average salary.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_23-25.png)

#### HAVING

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_23-31.png)

- Example: Show the median of the average salary that is greater than 100_000.

![alt text](images/sql-for-de/02-operators-and-functions/2026-07-04_23-53.png)

