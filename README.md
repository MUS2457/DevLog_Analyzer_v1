Developer Logging System

A simple command-line tool to log development sessions, track time spent on modules, and analyze productivity using Python and SQLite.

This project helps developers keep track of what they worked on, how long they spent, and view useful summaries such as total time per module or logs per month.

Features
Add development logs with different log levels
Track time spent during each session
Store logs in a SQLite database
View logs grouped by month
See which modules you spent the most time on
Count total logs or logs per module
Track total time spent coding
Simple CLI interface
Log Levels

The program supports the following log levels:

DEBUG
INFO
WARNING
ERROR

Each log contains:

log level
message
module name
time spent (minutes)
timestamp (automatic)
Example Workflow

Example session:

Enter log message from the list : ['DEBUG','INFO','WARNING','ERROR']
INFO

Enter message for the log :
Implemented search function

Enter module name that you have been working on :
ANALYSIS

Enter time spent on this session in minutes :
45

Before saving:

Do you want to save these logs? (y/n)
Menu

When running the program you will see:

Developer Logging System

1. Enter logs
2. Search logs by month
3. Top modules by time
4. Count logs
5. Count time spent
6. Exit
Example Output
Session summary
Session Summary
Total time this session: 120 minutes (2.0 hours)

Module: ANALYSIS
Sessions: 2
Time: 120 minutes (2.0 hours)
Top modules
Top Modules By Time

LOGIC -> 180 minutes (3.0 hours)
DATA -> 90 minutes (1.5 hours)
Project Structure
project/
│
├── main.py
│
├── DATA/
│   ├── SQL.py
│   ├── class_methods.py
│   └── input_data.py
│
├── LOGIC/
│   ├── analyse.py
│   └── tools.py
Responsibilities

DATA

Handles database connection
Data input
Logging class

LOGIC

Analysis functions
Search tools
Statistics

MAIN

Controls the program flow and menu
Technologies Used
Python
SQLite
Object Oriented Programming
Modular project structure
Purpose of the Project

This project was built as a practice exercise to improve:

Python project structure
working with SQLite databases
CLI program design
organizing code into modules
data analysis using SQL queries
Possible Future Improvements
Export logs to CSV or JSON
Add weekly statistics
Add productivity charts
Track daily coding streaks
Add filtering by module
