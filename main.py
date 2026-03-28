from DATA.SQL import create_connection, create_table, add_logs
from DATA.input_data import get_logging
from DATA.class_methods import Logging

from LOGIC.tools import search_date, top_modules_by_time
from LOGIC.analyse import logging_counter, count_timespent


def enter_logs(conn):
    logs = get_logging()

    if not logs:
        print("No logs entered.")
        return

    while True:
        save = input("Do you want to save these logs? (y/n): ").strip().lower()

        if save in ("y", "n"):
            break
        print("Invalid input. Enter y or n.")

    if save == "n":
        print("Logs were not saved.")
        return

    add_logs(conn, logs)

    total_minutes, total_hours = Logging.total_time(logs)
    module_data = Logging.total_per_module(logs)

    print("\nSession Summary")
    print(f"Total time this session: {total_minutes} minutes ({round(total_hours, 2)} hours)\n")

    for module, data in module_data.items():
        minutes = data["total"]
        sessions = data["sessions"]
        hours = round(minutes / 60, 2)

        print(f"Module: {module}")
        print(f"Sessions: {sessions}")
        print(f"Time: {minutes} minutes ({hours} hours)")
        print()


def show_logs_by_date(conn):
    result = search_date(conn)

    if not result:
        return

    data, hours = result

    print("\nLogs by Date\n")

    for log, modules in data.items():
        print(f"{log}")

        for module, total in modules.items():
            print(f"   {module} -> {total} minutes")

        print()

    print(f"Total hours this month: {hours}")


def show_top_modules(conn):
    modules = top_modules_by_time(conn)

    if not modules:
        return

    print("\nTop Modules By Time\n")

    for module, total in modules.items():
        hours = round(total / 60, 2)
        print(f"{module} -> {total} minutes ({hours} hours)")


def show_log_counter(conn):
    result = logging_counter(conn)

    if isinstance(result, dict):  # result contains module data
        print("\nLogs per module\n")

        for module, total in result.items():
            print(f"{module} -> {total}")

    else:
        print(f"\nTotal logs: {result}")


def show_time_counter(conn):
    result = count_timespent(conn)

    if isinstance(result, dict):
        print("\nTime spent per module\n")

        for module, total in result.items():
            hours = round(total / 60, 2)
            print(f"{module} -> {total} minutes ({hours} hours)")

    else:
        hours = round(result / 60, 2)
        print(f"\nTotal time spent: {result} minutes ({hours} hours)")


def main():
    conn = create_connection()
    create_table(conn)

    while True:

        print("\nDeveloper Logging System\n")
        print("1. Enter logs")
        print("2. Search logs by month")
        print("3. Top modules by time")
        print("4. Count logs")
        print("5. Count time spent")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            enter_logs(conn)

        elif choice == "2":
            show_logs_by_date(conn)

        elif choice == "3":
            show_top_modules(conn)

        elif choice == "4":
            show_log_counter(conn)

        elif choice == "5":
            show_time_counter(conn)

        elif choice == "6":
            print("Exiting program.")
            conn.close()
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()