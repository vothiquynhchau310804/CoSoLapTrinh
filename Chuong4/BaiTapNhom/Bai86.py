def TheTwelveDaysofChristmas(n):
    Days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = ['a partridge in a pear tree', 'two turtle doves', 'three French hens',
             'four calling birds', 'five gold rings', 'six geese a-laying',
             'seven swans a-swimming', 'eight maids a-milking',
             'nine ladies dancing', 'ten lords a-leaping',
             'eleven pipers piping', 'twelve drummers drumming']
    gifts = gifts[0:n]
    gifts.reverse()
    print("On the{0} day of Christmas".format(Days[n-1]))
    print("my true love sent to me:")
    if n==1:
        print("{0}.".format(gifts[0]))
    else:
        for i in range(n-1):
            print("{0},".format(gifts[i]))
        print("and{0}.".format(gifts[i]))
    print()
for n in range(1, 13):
    TheTwelveDaysofChristmas(n)