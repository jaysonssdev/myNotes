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