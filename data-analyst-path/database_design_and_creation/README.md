# Database Design and Creation
The aim of the project is to normalize a database from a set of CSVs by making extensive use of the Sqlite3 library.

We will be working with a file of *Major League Baseball games* from Retrosheet.
Retrosheet compiles detailed statistics on baseball games from the 1800s through to today. The main file we will be working from game_log.csv, has been produced by combining 127 separate CSV files from retrosheet, and has been pre-cleaned to remove some inconsistencies. 
The game_log has hundreds of data points on each game which will be normalized into several separate tables using SQL, providing a robust database of game-level statistics.

The major step areas are going to be the following:

- Import data into SQLite
- Design a normalized database schema
- Create tables for our schema
- Insert data into our schema

## Important Note on files'availability
The file in the repository do not include the full DB nor the original csv file for size purposes, becoming more than 500mb. In case you are interested to get those files please reach out or contact the Retrosheet team.