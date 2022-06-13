#FINDING THE DAY ON A SPECIFIC DATE
date=input("Enter the date whose day you want to know, year limit 1500-2700 (DD/MM/YYYY)- ")
num_date=int(date[slice(2)])
month=int(date[slice(3,5)])
year=int(date[slice(6,10)])
year_last_digit=int(date[slice(8,10)])
if (year % 4 == 0):
    if (year % 100 != 0):
        leap_year=True
    elif (year % 400 == 0):
        leap_year=True
    else:
        leap_year=False
else:
    leap_year=False
if (leap_year==True):
    january=4
    february=29
else:
    january=3
    february=28 
march,april,may,june,july,august,september,october,november,december=14,4,9,6,11,8,5,10,7,12
months=[january,february,march,april,may,june,july,august,september,october,november,december]   
date_month=(months[month-1])
if (1500<=year<1600 or 1900<=year<2000 or 2300<=year<2400):
    day_code=3
elif (1600<=year<1700 or 2000<=year<2100 or 2400<=year<2500):
    day_code=2
elif (1700<=year<1800 or 2100<=year<2200 or 2500<=year<2600):
    day_code=0
elif (1800<=year<1900 or 2200<=year<2300 or 2600<=year<2700):
    day_code=5
else:
    print("YOUR ENTERED YEAR CANNOT BE CALCULATED!!")
days=['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
remainder=(year_last_digit%12)
n=(months[month-1])
diff=(num_date - n )
value=(diff+day_code+(year_last_digit//12)+remainder+(remainder//4)) 
while (value>=6):
    value-=7
print(days[value])


