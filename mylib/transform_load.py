"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/grad_employment.csv"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("GradEmployment.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS GradEmployment")
    c.execute(
        """
        CREATE TABLE GradEmployment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            major_code TEXT,
            major TEXT,
            major_category TEXT,
            grad_total INTEGER,
            grad_sample_size INTEGER,
            grad_employed INTEGER,
            grad_full_time_year_round INTEGER,
            grad_unemployed INTEGER,
            grad_unemployment_rate REAL,
            grad_median INTEGER,
            grad_P25 INTEGER,
            grad_P75 INTEGER,
            nongrad_total INTEGER,
            nongrad_employed INTEGER,
            nongrad_full_time_year_round INTEGER,
            nongrad_unemployed INTEGER,
            nongrad_unemployment_rate REAL,
            nongrad_median INTEGER,
            nongrad_P25 INTEGER,
            nongrad_P75 INTEGER,
            grad_share REAL,
            grad_premium REAL
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO GradEmployment (
            major_code, major, major_category, grad_total, grad_sample_size,
            grad_employed, grad_full_time_year_round, grad_unemployed, grad_unemployment_rate, grad_median,
            grad_P25, grad_P75, nongrad_total, nongrad_employed, nongrad_full_time_year_round,
            nongrad_unemployed, nongrad_unemployment_rate, nongrad_median, nongrad_P25, nongrad_P75,
            grad_share, grad_premium
            ) 
            VALUES (?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, 
            ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "GradEmployment.db"