def logging_counter(conn):
    cursor = conn.cursor()
    counter_log_per_module = {}

    while True:
        print("1. Count all logs")
        print("2. Count logs by module")

        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input")
            continue

        if user_input == 1:

            cursor.execute("SELECT COUNT(*) AS total FROM logs")
            row = cursor.fetchone()

            total = row["total"]
            return total

        elif user_input == 2:

            cursor.execute("""
                SELECT module, COUNT(*) AS total
                FROM logs
                GROUP BY module
            """)

            rows = cursor.fetchall()

            if not rows:
                print("No logs found")
                continue

            for row in rows:
                module = row["module"]
                total = row["total"]
                counter_log_per_module[module] = total

            return counter_log_per_module

        else:
            print("Invalid input")


def count_timespent(conn):
    cursor = conn.cursor()

    counter_timespent_per_module = {}

    while True:
        print("1. Count all time spent")
        print("2. Count time spent per module")

        user_input = int(input("Enter your choice: "))

        if user_input == 1:

            cursor.execute("SELECT SUM(timespent) AS total FROM logs")

            rows = cursor.fetchall()

            if not rows:
                print("No logs found")
                continue

            for row in rows:
                total = row["total"]

                return total

        elif user_input == 2:

            cursor.execute("""SELECT module, SUM(timespent) AS total FROM logs GROUP BY module""")

            rows = cursor.fetchall()

            if not rows:
                print("No logs found")
                continue

            for row in rows:
                total = row["total"]
                modules = row["module"]

                counter_timespent_per_module[modules] = total

            return counter_timespent_per_module

        else:
            print("Invalid input")
            continue







