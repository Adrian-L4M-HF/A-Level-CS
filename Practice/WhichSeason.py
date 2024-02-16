#Which Season? - www.101computing.net/which-season/
#four seasons based on astronomical events known as the equinoxes and the solstices. 
from datetime import *

#Get Today's Date
today = date.today()
print("Today: " +  today.strftime('%A %d, %b %Y'))

#Find out the starting dates of each season:
thisYear = today.year
startOfSpring = date(thisYear,3,21) # March 21st
startOfSummer = date(thisYear,6,21) # June 21st
startOfAutumn = date(thisYear,9,21) # September 21st
startOfWinter = date(thisYear,12,21) # December 21st

if today >= startOfSpring and today < startOfSummer:
  print("We are in Spring.")
else:
  print("This is not Spring!")
  
if today >= startOfSummer and today < startOfAutumn:
  print("We are in Summmer.")
else:
  print("This is not Summer!")

if today >= startOfAutumn and today < startOfWinter:
  print("We are in Autumn.")
else:
  print("This is not Autumn!")

if today >= startOfWinter or today < startOfSpring:
  print("We are in Winter.")
else:
  print("This is not Winter!")