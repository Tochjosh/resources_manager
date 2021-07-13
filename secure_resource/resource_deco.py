from datetime import datetime
from auth import authenticate
from contextlib import contextmanager


def resource_deco(email, password):
    def middle(resource):
        def deco_wrapper():
            authenticated = authenticate(email, password)
            if authenticated:
                staff_name = authenticated['first_name'] + " " + authenticated['last_name']
                staff_role = authenticated['role']
                time = datetime.now()
                date_display = time.strftime("%x")
                time_display = time.strftime("%H:%M")

                if authenticated['role'] == 'admin' or authenticated['role'] == 'superadmin':
                    allowed = resource()

                    @contextmanager
                    def open_file(file, mode):
                        logger_list = open('access_granted.txt', 'a')
                        yield logger_list
                        logger_list.close()

                    with open_file("access_granted.txt", "a") as staff_log:
                        staff_log.write(
                            f"{staff_role} {staff_name} viewed company resources on {date_display} at {time_display}")
                    return allowed

                else:
                    with open("access_denied.txt", "a") as staff_log:
                        staff_log.write(
                            f"{staff_role} {staff_name} viewed company resources on {date_display} at {time_display}")
                    return "You are not allowed to view this resource"

            else:
                return "Only staffs can access this resource"

        return deco_wrapper

    return middle
