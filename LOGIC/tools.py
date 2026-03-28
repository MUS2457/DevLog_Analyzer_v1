def search_date(conn):
    cursor = conn.cursor()

    while True:
        data = {}

        user = input(
            "Enter date in format YYYY-MM or 'exit' to quit: "
        ).strip()

        if user.lower() == "exit":
            print("Exiting...")
            break

        cursor.execute("""
            SELECT log, module, SUM(timespent) AS total
            FROM logs
            WHERE strftime('%Y-%m', timestamp) = ?
            GROUP BY log, module
            ORDER BY log
        """, (user,))

        rows = cursor.fetchall()

        if not rows:
            print("No logs found for that date.")
            continue

        month_spent = 0

        for row in rows:
            log = row["log"]
            module = row["module"]
            total = row["total"]

            month_spent += total

            if log not in data:
                data[log] = {}

            data[log][module] = total

        month_hours = round(month_spent / 60, 2)

        return data, month_hours

def top_modules_by_time(conn):
    cursor = conn.cursor()

    while True:
        modules = {}

        user = input(
            "Enter how many top modules by time spent "
            "or 'exit' to quit: "
        ).strip()

        if user.lower() == "exit":
            print("Exiting...")
            break

        try:
            number = int(user)
        except ValueError:
            print("Invalid number.")
            continue

        cursor.execute("""
            SELECT module, SUM(timespent) AS total
            FROM logs
            GROUP BY module
            ORDER BY total DESC
            LIMIT ?
        """, (number,))

        rows = cursor.fetchall()

        if not rows:
            print("No modules found.")
            continue

        for row in rows:
            module = row["module"]
            total = row["total"]
            modules[module] = total

        return modules