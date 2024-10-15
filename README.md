# Mini_Project_5
[![CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project5/actions/workflows/cicd.yml)

This is the README for my Mini Project 5 for the IDS706 - Data Engineering Systems class at Duke University.

## Overview
The purpose of this project is to learn about and build an ETL-Query pipeline based on Python3 and SQLite3.

## Dataset
The dataset comes from FiveThirtyEight, an election polls, politics, and analysis website now acquired by ABC news. It contains a CSV file of detailed employment information regarding graduate students from different majors. Original data source is American Community Survey 2010-2012 Public Use Microdata Series. Link: https://github.com/fivethirtyeight/data/tree/master/college-majors

## Sample CRUD Operations
1. Create: `python main.py create_record ...` followed by 22 arguments
2. Read: `python main.py read_record`
3. Update: `python main.py update_record 1 ...` updates record with id of 1 followed by 22 arguments
4. Delete: `python main.py delete_record 1` deletes record with id of 1

For the 22 arguments, please refer to the specified dataset above.