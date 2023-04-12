def magicDates(day,month,year):
    if day*month==year%100:
        return True
    return False
def xuLy():
    for year in range(1900,2000):
        for month in range(1,13):
            for day in range(1,32):
                if magicDates(day,month,year):
                    print('{}/{}/{}'.format(day,month,year))
xuLy()