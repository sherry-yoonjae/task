import time
sleepTime = 1
def readMemInfo():
    res = {
    'total':0,
    'free':0,
    'buffers':0,
    'cached':0
    }
    f = open('/proc/meminfo')
    lines = f.readlines()
    f.close()
    i = 0
    for line in lines:
        if i == 4:
            break
        line = line.lstrip()
        memItem = line.lower().split()
        if memItem[0] == 'memtotal:':
            res['total'] = long(memItem[1])
            i = i +1 
            continue
        elif memItem[0] == 'memfree:':
            res['free'] = long(memItem[1])
            i = i +1
            continue
        elif memItem[0] == 'buffers:':
            res['buffers'] = long(memItem[1])
            i = i + 1
            continue
        elif memItem[0] == 'cached:':
            res['cached'] = long(memItem[1])
            i = i + 1
            continue
    return res

def calcMemUsage(counters):

    used = counters['total'] - counters['free'] - counters['buffers']-counters['cached']
    total = counters['total']
    usage = float(used)/total*100
    return usage

if __name__ == '__main__':

    # while 1:
    time.sleep(sleepTime)
    begin = time.time()
    counters = readMemInfo()
    print '--------------'
    print "total: %f" %(counters['total'])
    print "used: %f"  %(counters['total'] - counters['free'] - counters['buffers']-counters['cached'])
    rate = calcMemUsage(counters)
    end = time.time()
    print ("memory usage:%.2f%%" %(rate))
    print ("time:%f" %(end- begin))
    print '---------------'