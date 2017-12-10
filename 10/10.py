import sys

input = '''147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'''
##input = '3,4,1,5'

curr_pos = 0
skip_size = 0

SOURCE_SIZE = 256
values = range(SOURCE_SIZE)

def init():
    global curr_pos, skip_size, values
    curr_pos = 0
    skip_size = 0
    values = range(SOURCE_SIZE)

def perturb(l):
    global values, curr_pos, skip_size
    if (l > 1):
        end = curr_pos + l
        if (end > SOURCE_SIZE):
            lead = end - SOURCE_SIZE
            data = values[curr_pos:] + values[:lead]
            data = data[::-1]
            values = data[l - lead:] + values[lead:curr_pos] + data[:l-lead]
        else:
            first = values[:curr_pos]
            reversed = values[curr_pos:curr_pos + l]
            last = values[curr_pos + l:]
            values = first + reversed[::-1] + last
    curr_pos = (curr_pos + l + skip_size) % SOURCE_SIZE
    skip_size += 1

lengths = map(int, input.split(','))
init()
for l in lengths:
    perturb(l)

print "Part 1", values[0] * values[1]

def dense_hash(values):
    dense = []
    assert(len(values) == SOURCE_SIZE)
    for i in xrange(0, SOURCE_SIZE, 16):
        dense.append(reduce(lambda x, y: x ^ y, values[i:i+16]))
    return dense

def hash(input):
    init()
    for round in xrange(64):
        for b in input + suffix:
            l = ord(b)
            perturb(l)

    d_hash = dense_hash(values)
    return ''.join(map(lambda x: '{:02x}'.format(x), d_hash))

suffix = ''.join(map(chr, [17, 31, 73, 47, 23]))

if False:
    test_inputs = [('', 'a2582a3a0e66e6e86e3812dcb672a272'),
                   ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
                   ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
                   ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
                   ]

    for test, expected in test_inputs:
        result = hash(test)
        print
        print 'input: "%s"' % test
        print result, len(result)
        print expected, len(expected)
        print '\t', result == expected

print
print "Part 2",
print hash(input)
    