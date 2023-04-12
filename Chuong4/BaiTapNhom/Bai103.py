def magicDates(day,month,year):
    if day*month==year%100:
        return True
    return False
def xuLy():
    for year in range(1900,2000):
        for month in range(1,13):
            if month==2:
                if (year%4==0 and year%100!=0) or year%400==0:
                    day=29
                else:
                    day=28
            elif month in [1,3,5,7,8,10,12]:
                day=31
            else:
                day=30
            for day in range(1,day+1):
                if magicDates(day,month,year):
                    print('{}/{}/{}'.format(day,month,year))
xuLy()