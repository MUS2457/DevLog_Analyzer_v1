def get_log () :
    list_log = ['DEBUG','INFO','WARNING','ERROR']

    while True:
        log = input(f"Enter log message from the list : {list_log} or "
                    f" 'done' to finish 'exit' to quit ").strip()

        if log.lower() in ('done','exit') :
            return log.lower()
        elif log.upper() not in list_log :
            print(f"Invalid log message : {log}")
            continue

        return log.upper()


def get_message(log) :
    while True:
        message = input(f"Enter message for the log : {log} or 'exit' to quit ").strip()

        if any(char.isdigit() for char in message) or not message :
            print(f"Invalid message : {message}")
            continue

        return message


def get_module() :
    while True:
        module = input("Enter module name that you have been working on : ").strip()

        if not module or any(char.isdigit() for char in module) :
            print(f"Invalid module name : {module}")
            continue

        return module.upper()

def get_time_spent() :
    while True:
        try :
            time = int(input(f"Enter time spent on this session in minutes : "))

            if time <= 0 :
                print(f"Invalid time format : {time}")
                continue
            return time

        except ValueError :
            print(f"Invalid time format :")



