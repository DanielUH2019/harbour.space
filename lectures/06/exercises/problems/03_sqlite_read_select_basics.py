"""Problem 03: Read data from `students` (SELECT basics).

Task:
1. Select all columns from all rows
2. Select only `name` and `email`
3. Select one row by email (`ana@example.com`) using parameterized query
4. Print query results in readable form
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT * FROM students
    # rows = cur.fetchall()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("rows: ", rows)
    print()
    # TODO: SELECT name, email FROM students
    # name_email_rows = cur.fetchall()
    cur.execute("SELECT name, email FROM students")
    name_email_rows = cur.fetchall()
    print("name email rows: ", name_email_rows)
    print()
    # TODO: SELECT one row for ana@example.com
    # one_row = cur.fetchone()

    cur.execute("SELECT * FROM students WHERE email = 'ana@example.com'")
    one_row = cur.fetchone()
    print("one row", one_row)
    conn.close()


if __name__ == "__main__":
    main()
