def pay(hourly_wage,work_hour):
    if work_hour<=40:
        pay= hourly_wage*work_hour
        return pay
    if work_hour>40:
        pay= (hourly_wage*1.5*work_hour)
        return pay
hourly_wage= int(input('Enter hourly wage: '))
work_hour= int(input('Enter number of hours employee worked in the last week: '))
print(pay(hourly_wage,work_hour))
