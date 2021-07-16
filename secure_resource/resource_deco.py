from datetime import datetime
from auth import authenticate


def resource_deco(email, password):
    def middle(resource):  # if decorator takes more than one parameter, then an intermediate func. is used.
        def deco_wrapper():
            # Authentication of the user is verified below,
            # using the authentication function that loops through the database of staffs
            authenticated_staff = authenticate(email, password)

            if authenticated_staff:
                # if the user passes for a staff, the details are extracted below
                staff_name = authenticated_staff['first_name'] + " " + authenticated_staff['last_name']
                staff_role = authenticated_staff['role']
                time = datetime.now()  # datetime module is imported and used here to get the present time

                # datetime is scrapped for time and date below
                date_display = time.strftime("%x")
                time_display = time.strftime("%H:%M")

                if authenticated_staff['role'] == 'admin' or authenticated_staff['role'] == 'superadmin':
                    # the admin and superadmin is allowed here to access the company's resource.
                    company_resource = resource()

                    with open("access_granted.txt", "a") as staff_log:
                        staff_log.write(
                            f"\n{staff_role} {staff_name} viewed company resources on {date_display} at {time_display}")
                    return company_resource  # company resource is made available here

                else:
                    # staffs below admin and superadmin level are denied access here, and their details logged here.
                    with open("access_denied.txt", "a") as staff_log:
                        staff_log.write(
                            f"\n{staff_role} {staff_name} viewed company resources on {date_display} at {time_display}")
                    return "You are not allowed to view this resource"
                    # an access denied message is returned to the staff here

            else:  # anonymous person is denied access here
                return "Only staffs can access this resource"

        return deco_wrapper

    return middle
