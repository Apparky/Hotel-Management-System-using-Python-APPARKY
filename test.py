import datetime

check_in_date = "20/10/2022"
check_out_date = "2/11/2022"

check_in_date = datetime.datetime.strptime(check_in_date, "%d/%m/%Y")
check_out_date = datetime.datetime.strptime(check_out_date, "%d/%m/%Y")

no_of_days = (check_out_date - check_in_date).days

print(no_of_days)