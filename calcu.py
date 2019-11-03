while True:
    year = int(float(input("Enter year1:")))
    if year<int(0) or year<=int(0):
        print("Error. Please try again")
    else:
        print(year)
        break
while True:
    month = int(float(input("Enter month1:")))
    if month>int(12) or month<=int(0):
        print("Error. Please try again")
    else:
        print(month)
        break
    
while True:
    day = int(float(input("Enter day1:")))
    if month == int(2) and year%4==0:
            if day > 29 or day<0 or day<=int(0):
                print("Try again")
            else:
                print(day)
                break
    elif month ==2 and year%4!=0:
        if day>28 or day<=int(0):
            print("Error")
        else:
            print(day)
            break
    elif day>int(31) or day<=int(0):
       print("Error. Please try again")
    elif month == int(9) or int(4) or int(6) or int(11) :
        if day >= int(30) or day<=int(0):
            print("Error.")
        else:
            print(day)
            break
    
while True:
    hours = int(float(input("Enter hours1:")))
    if hours == 24:
        hours = int(00)
    if hours>int(24) or hours <int(0):
        print("Error. Please try again")
    else:
        print(hours)
        break
while True:
    minutes = int(float(input("Enter minutes1:")))
    if minutes>int(60) or minutes<int(0):
        print("Error. Please try again")
    else:
        print(minutes)
        break
while True:
    seconds = int(float(input("Enter seconds1:")))
    if seconds>int(60) or seconds<int(0):
        print("Error. Please try again")
    else:
        print(seconds)
        break
    
while True:
    year1 = int(float(input("Enter year2:")))
    if year1<int(0) or year1<=int(0):
        print("Error. Please try again")
    else:
        print(year1)
        break
while True:
    month1 = int(float(input("Enter month2:")))
    if month1>int(12) or month1<=int(0) or month1<=int(0):
        print("Error. Please try again")
    else:
        print(month1)
        break
while True:
    day1 = int(float(input("Enter day2:")))
    if month1 == int(2) and year1%4==0:
            if day1 > 29 or day1<0 or day1<=int(0):
                print("yes")
            else:
                print(day1)
                break
    elif month1 ==2 and year1%4!=0:
        if day1>28 or day1<=int(0):
            print("Error")
        else:
            print(day1)
            break
    elif day1>int(31) or day1<=int(0):
       print("Error. Please try again")
    elif month1 == int(9) or int(4) or int(6) or int(11):
        if day1 >= int(30) or day1<=int(0):
            print("Error.")
        else:
            print(day1)
            break
while True:
    hours1 = int(float(input("Enter hours2:")))
    if hours1>int(24) or hours1 <int(0):
        print("Error. Please try again")
    else:
        print(hours1)
        break
while True:
    minutes1 = int(float(input("Enter minutes2:")))
    if minutes1>int(60) or minutes1<int(0):
        print("Error. Please try again")
    else:
        print(minutes1)
        break
while True:
    seconds1 = int(float(input("Enter seconds2:")))
    if seconds1>int(60) or seconds1<int(0): 
        print("Error. Please try again")
    else:
        print(seconds1)
        break

if month or month1 == 4 or 6 or 9 or 11:
    sumyear = year*31536000
    summonth = month *2592000
    sumday = day * 86400
    sumhours = hours * 3600
    summinutes = minutes * 60
    
    sumyear1 = year1*31536000
    summonth1 = month1 *2592000
    sumday1 = day1 * 86400
    sumhours1 = hours1 * 3600
    summinutes1 = minutes1 * 60

if month or month1 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    sumyear = year*31536000
    summonth = month * 2678400
    sumday = day * 86400
    sumhours = hours * 3600
    summinutes = minutes * 60
    
    sumyear1 = year1*31536000
    summonth1 = month1 *2678400
    sumday1 = day1 * 86400
    sumhours1 = hours1 * 3600
    summinutes1 = minutes1 * 60

if month or month1 == 2:
    sumyear = year*31536000
    summonth = month * 2352000
    sumday = day * 86400
    sumhours = hours * 3600
    summinutes = minutes * 60
    
    sumyear1 = year1*31536000
    summonth1 = month1 *2352000
    sumday1 = day1 * 86400
    sumhours1 = hours1 * 3600
    summinutes1 = minutes1 * 60

sumsec = sumyear + summonth + sumday + sumhours + summinutes + seconds

sumsec1 = sumyear1 + summonth1 + sumday1 + sumhours1 + summinutes1 + seconds1

print(sumsec1 , sumsec)

totalsec = sumsec1 - sumsec

print(totalsec)
years = 0
months = 0
days = 0
hours = 0
minutes = 0
sumsecond = 0
while True:
    if totalsec >= 31536000:
        years+=1
        totalsec-=31536000
        if totalsec <= 0:
            break
    elif totalsec >= 2592000:
        months+=1
        totalsec-=2592000
        if totalsec <= 0:
            break
    elif totalsec >= 86400:
        days+=1
        totalsec-= 86400
        if totalsec <= 0:
            break
    elif totalsec >= 3600:
        hours+=1
        totalsec-=3600
        if totalsec <= 0:
            break
    elif totalsec >= 60:
        minutes+=1
        totalsec-=60
        if totalsec <= 0:
            break
    elif totalsec >=1:
        sumsecond+=1
        totalsec-=1
        if totalsec <= 0:
            break
print("Years {}, Month {}, Days {}, Hours {}, Minutes {}, Second {}".format(years,months,days,hours,minutes,sumsecond))
    
