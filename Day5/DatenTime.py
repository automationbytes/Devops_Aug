from datetime import datetime

currenttime = datetime.now()
print(currenttime)
#date
print(currenttime.strftime("%a")) #Sat
print(currenttime.strftime("%A")) #Saturday
print(currenttime.strftime("%d")) #03


#month
print(currenttime.strftime("%b")) #Sep
print(currenttime.strftime("%B")) #September
print(currenttime.strftime("%m")) #09

#year
print(currenttime.strftime("%y")) #22
print(currenttime.strftime("%Y"))#2022

#hours
print(currenttime.strftime("%I"), currenttime.strftime("%p"))
print(currenttime.strftime("%H"))

#mins
print(currenttime.strftime("%M"))

#Sec
print(currenttime.strftime("%S"))