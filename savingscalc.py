earningsgoal = float(input("Enter the amount of money you want to save: $"))


months = round((earningsgoal / 12), 2)
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(months) + " dollars per month.")


weeks = round((earningsgoal / 52), 2)
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(weeks) + " dollars per week.")


days = round((earningsgoal / 365), 2)
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(days) + " dollars per day.")