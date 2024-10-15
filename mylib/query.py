"""Query the database"""
import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("GradEmployment.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    major_code, major, major_category, grad_total, grad_sample_size,
            grad_employed, grad_full_time_year_round, grad_unemployed, grad_unemployment_rate, grad_median,
            grad_P25, grad_P75, nongrad_total, nongrad_employed, nongrad_full_time_year_round,
            nongrad_unemployed, nongrad_unemployment_rate, nongrad_median, nongrad_P25, nongrad_P75,
            grad_share, grad_premium
):
    """create example query"""
    conn = sqlite3.connect("GradEmployment.db")
    c = conn.cursor()
    c.execute(
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
        (major_code, major, major_category, grad_total, grad_sample_size,
            grad_employed, grad_full_time_year_round, grad_unemployed, grad_unemployment_rate, grad_median,
            grad_P25, grad_P75, nongrad_total, nongrad_employed, nongrad_full_time_year_round,
            nongrad_unemployed, nongrad_unemployment_rate, nongrad_median, nongrad_P25, nongrad_P75,
            grad_share, grad_premium),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO GradEmployment VALUES (
            {major_code}, {major}, {major_category}, {grad_total}, {grad_sample_size},
            {grad_employed}, {grad_full_time_year_round}, {grad_unemployed}, {grad_unemployment_rate}, {grad_median},
            {grad_P25}, {grad_P75}, {nongrad_total}, {nongrad_employed}, {nongrad_full_time_year_round},
            {nongrad_unemployed}, {nongrad_unemployment_rate}, {nongrad_median}, {nongrad_P25}, {nongrad_P75},
            {grad_share}, {grad_premium});"""
    )


def update_record(
    record_id, 
    major_code, major, major_category, grad_total, grad_sample_size,
            grad_employed, grad_full_time_year_round, grad_unemployed, grad_unemployment_rate, grad_median,
            grad_P25, grad_P75, nongrad_total, nongrad_employed, nongrad_full_time_year_round,
            nongrad_unemployed, nongrad_unemployment_rate, nongrad_median, nongrad_P25, nongrad_P75,
            grad_share, grad_premium
):
    """update example query"""
    conn = sqlite3.connect("GradEmployment.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE GradEmployment 
        SET major_code=?, major=?, major_category=?, grad_total=?, grad_sample_size=?,
            grad_employed=?, grad_full_time_year_round=?, grad_unemployed=?, grad_unemployment_rate=?, grad_median=?,
            grad_P25=?, grad_P75=?, nongrad_total=?, nongrad_employed=?, nongrad_full_time_year_round=?,
            nongrad_unemployed=?, nongrad_unemployment_rate=?, nongrad_median=?, nongrad_P25=?, nongrad_P75=?,
            grad_share=?, grad_premium=?
        WHERE id=?
        """,
        (
            major_code, major, major_category, grad_total, grad_sample_size,
            grad_employed, grad_full_time_year_round, grad_unemployed, grad_unemployment_rate, grad_median,
            grad_P25, grad_P75, nongrad_total, nongrad_employed, nongrad_full_time_year_round,
            nongrad_unemployed, nongrad_unemployment_rate, nongrad_median, nongrad_P25, nongrad_P75,
            grad_share, grad_premium, record_id
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE GradEmployment SET 
        major_code={major_code}, major={major}, major_category={major_category}, grad_total={grad_total}, grad_sample_size={grad_sample_size},
        grad_employed={grad_employed}, grad_full_time_year_round={grad_full_time_year_round}, grad_unemployed={grad_unemployed}, grad_unemployment_rate={grad_unemployment_rate}, grad_median={grad_median},
        grad_P25={grad_P25}, grad_P75={grad_P75}, nongrad_total={nongrad_total}, nongrad_employed={nongrad_employed}, nongrad_full_time_year_round={nongrad_full_time_year_round},
        nongrad_unemployed={nongrad_unemployed}, nongrad_unemployment_rate={nongrad_unemployment_rate}, nongrad_median={nongrad_median}, nongrad_P25={nongrad_P25}, nongrad_P75={nongrad_P75},
        grad_share={grad_share}, grad_premium={grad_premium}
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("GradEmployment.db")
    c = conn.cursor()
    c.execute("DELETE FROM GradEmployment WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM GradEmployment WHERE id={record_id};")


def read_record():
    """read data"""
    conn = sqlite3.connect("GradEmployment.db")
    c = conn.cursor()
    c.execute("SELECT * FROM GradEmployment LIMIT 10")
    data = c.fetchall()
    log_query("SELECT * FROM GradEmployment LIMIT 10;")
    return data