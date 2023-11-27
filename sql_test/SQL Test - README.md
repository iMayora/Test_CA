# SQL Test for Condor Agency Analytics Department

## Overview
This repository contains my solution to the SQL test provided as part of the recruitment process for the Analytics Department at Condor Agency. The test involves writing an SQL query that manipulates and analyzes data from two tables: `invoices` and `invoice_items`.

## Test Description
The task was to write an SQL query to create a new view from the `invoices` and `invoice_items` tables. The new view should display the total amount of each invoice and distribute this amount into three categories: "carnes", "cereales", and "others". This categorization is based on the description provided in the `invoice_items` table.

## Repository Contents
- `SQL_test.sql`: The SQL script containing the query to create the required view.
- `invoices.csv`: A CSV file representing the 'invoices' table.
- `invoices_items.csv`: A CSV file representing the 'invoice_items' table.
- `query_result - invoices_view.csv`: The resulting CSV file after running the query, showing the new view with the categorized amounts.

## Running the Query
The SQL script can be run in any standard SQL environment that supports multi-table queries. Import the CSV files into your SQL database, and execute the script found in `SQL_test.sql` to view the results.



## Acknowledgements
- Special thanks to the Condor Agency Analytics Department for providing this opportunity and challenge.