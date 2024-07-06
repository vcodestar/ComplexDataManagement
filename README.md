# Group-by with Aggregation, Merge Join, and Composite Query

This repository contains three Python programs that perform various database operations on CSV files.

## Part 1: Group-by with Aggregation

This program reads a CSV file, groups by a specified attribute, performs an aggregation function (sum, min, or max), and writes the results to `O1.csv`.


## Part 2: Merge join

This program reads two sorted CSV files (R.csv and S.csv), performs a natural join on them, and writes the results to O2.csv.

## Part 3: Composite Query

This program reads two CSV files, filters R.csv based on a condition (R.C = 7), performs a join with S.csv, computes an aggregate (sum of S.E), and writes the results to O3.csv.

## Top-K Join Algorithms for Demographic Data

https://kdd.ics.uci.edu/databases/census-income/census-income.html

Dataset
The dataset used in this project is obtained from the UCI Machine Learning Repository. It consists of demographic data from the United States, divided into two sorted files:

males_sorted: Contains records of males sorted by instance weight.
females_sorted: Contains records of females sorted by instance weight.
Each record in these files begins with an ID indicating its position in the original dataset (census-income.data), followed by demographic fields such as age, class of worker, marital status, etc.

## Algorithm A: Hash-based Rank Join (HRJN)
Implementation Details
Algorithm Overview: Implemented the HRJN algorithm as described in the provided specifications.
Functionality: The algorithm reads through males_sorted and females_sorted files alternately. It uses hash tables to organize records by age, excludes married individuals and minors, calculates scores (sum of instance weights) for valid pairs with the same age, and maintains a max heap to track top-k pairs.
Output: The program prints the top-k pairs along with their scores, as well as the execution time.


## Algorithm B: Alternative Approach
Implementation Details
Algorithm Overview: Implemented an alternative top-k join algorithm where records from males_sorted are stored in a hash table based on age. It iterates through females_sorted, performs lookups in the hash table for matching age groups, calculates scores, and maintains a min heap for top-k pairs.
Output: The program prints the top-k pairs along with their scores, as well as the execution time.
