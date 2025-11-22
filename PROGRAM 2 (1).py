'''2.An App for Mobile hosting provider charges- $0.51 per hour . 
 how much does it cost to operator per day, per week, per month? 
how many days can i operate one server with$918?'''
cost=0.51
per_day=cost*24
per_week=per_day*7
per_month=per_week*4
print("Cost per day: $",per_day)
print("Cost per week: $",per_week)
print("Cost per month: $",per_month)
budget=918
days=budget/per_day    
print("Number of days one server can operate with $918: ",days )