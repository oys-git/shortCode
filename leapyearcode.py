#year = int(input("Enter a year: "))
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return False
  else:
    return False
#output = is_leap(year)
#print(output)
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  months = list(range(1, 13))
  if is_leap(year):
    return 29
  else:
    for i in months:
      if i == month:
        month -= 1
    return month_days[month]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
