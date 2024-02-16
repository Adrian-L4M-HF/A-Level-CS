#Days left until Summer - www.101computing.net/days-until-summer/
from datetime import *

#Get Today's Date
today = date.today()
print("Today: " +  today.strftime('%d, %b %Y'))

#Find out the date of next summer:
thisYear = today.year
Christmas = date(thisYear,12,25) # Dec 25
Summer = date(thisYear,6,21) # June 21

"""Original Code from Website
if today < Christmas:
  print("Next Christmas: " +  Christmas.strftime('%d, %b %Y'))
  #Calculate the number of days till Christmas
  delta = (Christmas - today).days
  print(str(delta) + " days left until Christmas!")  
elif today == Christmas:
  print("Today is Chirstmas Day!")
else:
  #We've passed this year's Christmas, we will need to wait for next year!
  nextXmas = date(thisYear+1,12,25)
  print("Next Christmas: " +  nextXmas.strftime('%d, %b %Y'))
  delta = (nextXmas - today).days
  print(str(delta) + " days left until next Chistmas!")
"""
def from_today_to_(special_date):
    if today < special_date:
        print(f"Next one is on {special_date.strftime('%d, %b %Y')}")
        days_to_special_date = str((special_date - today).days)
        return (f"{days_to_special_date} days left until {special_date}!")
    elif today == special_date:
        return (f"Today is {special_date}!")
    else: 
        next_special_date = date(thisYear+1)
        print(f"Next one is on {next_special_date.strftime('%d, %b %Y')}")
        days_to_next_special_date = str((next_special_date - today).days)
        return (f"{days_to_next_special_date} days left until next {special_date}!")
        
print(from_today_to_(Summer))
print(from_today_to_(Christmas))     