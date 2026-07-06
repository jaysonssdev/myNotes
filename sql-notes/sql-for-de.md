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

<br>
<br>
<br>

## 3. Terminal Intro

### Shell Types by Operating System

![alt text](images/sql-for-de/03-terminal-intro/2026-07-05_00-09.png)

### Basic Commands

![alt text](images/sql-for-de/03-terminal-intro/2026-07-05_00-11.png)
![alt text](images/sql-for-de/03-terminal-intro/2026-07-05_00-17.png)

<br>
<br>
<br>

## 4. Local DuckDB Intro

![alt text](images/sql-for-de/04-local-duckdb/2026-07-05_12-06.png)

### Installation Website

- Install duckdb from this website: https://motherduck.com/docs/getting-started/interfaces/connect-query-from-duckdb-cli/
- The reason that we should install the version in this website is because it is the version that **MotherDuck** supports.
- Or install it using https://github.com/NiclasHaderer/duckdb-version-manager to easily manage the versions.

### Basic Commands (in Terminal)
- `duckdb` - to run duckdb locally
- `.quit` or `.exit` - to exit duckdb
- `.help` - for usage hints
- `-c` - is used so that we don't need to enter duckdb cli, and we can just run a command. Example: `duckdb -c "SELECT 42 as answer"`

### Local DuckDB Databases
- `duckdb <FILENAME>` - to create a database file. Make sure that you go to the folder first that you want your database file to be created in. Example:
```bash
cd ~/Desktop/Notes/QA/duckdb-practice/
duckdb jobs.duckdb

# Now you created a database and your inside a duckdb session
# You can create a simple table named 'jobs' with 2 columns 'id' and 'job'
CREATE TABLE jobs (
       id INTEGER,
       job VARCHAR
       );

# You can check and see your newly created table
.tables

# You can make a simple query
SELECT * FROM jobs;

# To insert values inside the columns
INSERT INTO jobs VALUES
(1, 'Data Analyst'),
(2, 'Data Scientist'),
(3, 'Data Engineer');

# You can now exit and everything will be saved
.quit

# To open again this database file
duckdb jobs.duckdb
```

### Local DuckDB UI
- `duckdb -ui` - to open the duckdb UI in a new browser.
- `duckdb -ui <FILENAME>` - to open a database file with UI. Example: `duckdb -ui jobs.duckdb`. Now you can create a new notebook then query. `SELECT * FROM jobs;`
- **Sign In to MotherDuck** using the account that you created earlier.

### Local DuckDB Connect to MotherDuck
- `duckdb md:<DATABASE>` - run this in your terminal to open a database from your MotherDuck account. Example: `duckdb md:data_jobs`. Accept and confirm the token for now.
- To test, run:
```bash
SELECT DISTINCT(job_title_short)
    FROM job_postings_fact;
```

<br>
<br>
<br>

## 5. VS Code Intro

### Installation Website
- Go to https://code.visualstudio.com/ to download the right installer for your OS.

### VS Code SQL Setup
#### Create a key binding
- Press `ctrl + shift + P`
- The select **Preferences: Open Keyboard Shortcuts**
- Select **Terminal: Run Selected Text In Active Terminal**
- Assign for Keybinding `shift + enter`

#### Setting up DuckDB & MotherDuck
- Go to your MotherDuck account (app.motherduck.com)
- Click your 'Organization' on the top left corner then click **Settings**.
- On the left side, under INTEGRATIONS, click **Access Tokens**
- Click "**+ Create token**" to create a token that does not expire.
- Click **Copy** to copy the characters, then click 'Close'.
- Temporary Authentication (NOT RECOMMENDED):
    - Go back to VS Code Terminal.
    - Run `export motherduck_token="paste_your_token_here"`
    - You can now run `duckdb md:<DATABASE>` and you will be authenticated. But if you close the terminal, you have to repeat the whole process again.
- Permanent Authentication (RECOMMENDED):
    - Open your `.bashrc` file in ~
    - Put the `export motherduck_token="paste_your_token_here"`
    - Save then run `source .bashrc`

### How to run a SQL file in VS Code
- Open VS Code, then open your project folder.
- Open your sql file (*.sql) by clicking it.
- Open a terminal inside VS Code (**ctrl + `**).
- For example, run `duckdb md:data_jobs` to connect to your database in MotherDuck.
- Once you're connected in duckdb, select all the code from your sql file, then press `Shift + Enter` to automatically run it in the terminal.

<br>
<br>
<br>

## 6. Data Modeling & JOINs

### Database Hierarchy

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-19.png)

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-23.png)

#### Tables

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-27.png)

#### Schema

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-35.png)

#### Database

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-38.png)

<br>

### Entity Relationship Diagram (ERD)

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-49.png)

#### Table Diagram

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_12-50.png)

#### Relationship Diagram

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-02.png)

- **One-to-One**

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-03.png)

- **One-to-Many** (Most Common)

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-05.png)

- **Many-to-Many** (Least Common)

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-09.png)

<br>

### Database Metadata

#### Information Schema
- Information schema is basically a collection of read-only views that tells us information about the metadata inside of our database. We can look at things like tables, columns, views, or table constraints.

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-13.png)

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-31.png)

- **DESCRIBE** - run `DESCRIBE <table_name>` to see the different columns associated with that table. Example:

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-42.png)

<br>

### JOINs
- used to join the tables together and perform analysis with that.
- most commonly used are **LEFT JOIN** and **INNER JOIN**

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-47.png)

#### LEFT JOIN (most common)
- Returns all rows from LEFT and only matching from RIGHT.
- Example: 
    - Table A: job_postings_fact
    - Table B: company_dim

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_13-53.png)

```sql
SELECT
    jpf.job_id,              -- get 'job_id' column from 'job_postings_fact' table
    cd.name AS company_name, -- get 'name' column from 'company_dim' table
    jpf.job_title_short      -- get 'job_title_short' column from 'job_postings_fact' table
FROM
    job_postings_fact AS jpf -- alias for 'job_postings_fact' table 
LEFT JOIN company_dim AS cd
    ON jpf.company_id = cd.company_id; -- joining them using their related columns 'company_id'
```

- Same query as above WITHOUT the aliases:
```sql
SELECT
    job_postings_fact.job_id,
    company_dim.name,
    job_postings_fact.job_title_short
FROM
    job_postings_fact
LEFT JOIN company_dim
    ON job_postings_fact.company_id = company_dim.company_id;
```

#### RIGHT JOIN (least common)
- Preserving or keeping all records from Table B.

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_19-31.png)

#### INNER JOIN (also most common)
- The original default join in SQL, so some people just use `JOIN` instead of `INNER JOIN`.
- Returns only matching rows from both tables.

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_19-38.png)

#### FULL OUTER JOIN
- Some people just use `FULL JOIN`

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_19-42.png)

<br>

### SQL Clause Order 

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_22-05.png)

### SQL Execution Order

![alt text](images/sql-for-de/06-data-modeling-and-joins/2026-07-06_22-08.png)