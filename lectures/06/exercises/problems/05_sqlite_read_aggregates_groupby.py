"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT COUNT(*) FROM students
    cur.execute("SELECT COUNT(*) FROM students")
    count = cur.fetchall()
    print("count ", count)
    print()
    # TODO: SELECT AVG(age) FROM students
    cur.execute("SELECT AVG(age) FROM students")
    avgerage = cur.fetchall()
    print("average ", avgerage)
    print()
    # TODO: SELECT MIN(age), MAX(age) FROM students
    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    min_max = cur.fetchall()
    print("min_max: ", min_max)
    print()
    # TODO: SELECT track, COUNT(*) FROM students GROUP BY track
    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    track_count = cur.fetchall()
    print('track count: ', track_count)
    conn.close()


if __name__ == "__main__":
    main()
