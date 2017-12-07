data = '''14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'''
##data = '0 2  7 0'
banks = [ int(x) for x in data.split()]

def biggest_bank(banks):
    tgt = 0
    size = banks[0]
    for i in xrange(1, len(banks)):
        s = banks[i]
        if s > size:
            tgt = i
            size = s
    return tgt

def redistribute(banks, source):
    count = len(banks)
    values = banks[source]
    banks[source] = 0
    tgt = (source + 1) % count
    while values:
        banks[tgt] += 1
        values -= 1
        tgt = (tgt + 1) % count

config_times = {}
configs = set()
configs.add(tuple(banks))
config_times[tuple(banks)] = 0
print configs

redist = 0

print banks
while True:
    source = biggest_bank(banks)
    redistribute(banks, source)
    redist += 1
##    print redist, banks
    c = tuple(banks)
    if (c in configs):
        break
    config_times[c] = redist
    configs.add(c)

print redist
print redist - config_times[c]
