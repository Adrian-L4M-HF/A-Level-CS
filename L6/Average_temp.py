def average_temp(temps_list):
    total_temp = 0
    for temp in temps_list:
        total_temp += temp
    average_temp = total_temp / len(temps_list)
    return average_temp

finish = False
max_temps = []
min_temps = []
while finish == False:
    max_temp = input("Maximum Temperature: ")
    if max_temp == 999:
        finish = True
    min_temp = input("Minimum Temperature: ")
    max_temps.append(max_temp)
    min_temps.append(min_temp)
    average_temp = average_temp(max_temps)
    
        
        



