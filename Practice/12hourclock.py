#12 Hour Clock Time Convertor - www.101computing.net/12-hour-clock/ 

time=input("Enter a time in the 24-hour format (e.g 18:36): ")
timeArray = time.split(":")

hours = int(timeArray[0])
minutes = int(timeArray[1])

if hours > 24 or minutes > 119:
    raise ValueError    
if minutes >= 60:
    minutes -= 60
    hours += 1
if hours == 24: 
    hours = 0

ampm = ""
if hours == 12:
  ampm = "PM"
elif hours == 0:
  ampm = "AM"
  hours=12
elif hours >= 12:
  ampm ="PM"
  hours = hours - 12
else:
  ampm = "AM"
  

  
print(f"{hours}:{minutes} {ampm}")