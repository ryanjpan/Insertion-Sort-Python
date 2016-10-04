def insertionsort(list):
    for i in range(0, len(list)):
        j = i
        val = list[i]
        while(val < list[j-1] and j > 0):
            list[j] = list[j-1]
            j -= 1
        list[j] = val

import random
import datetime

a = range(1, 10001)
random.shuffle(a)
t1 = datetime.datetime.now()
insertionsort(a)
t2 = datetime.datetime.now()
if(all(a[i] <= a[i+1] for i in xrange(len(a)-1))):
    print 'Sorted Correctly'
print 'Time:', t2 - t1
