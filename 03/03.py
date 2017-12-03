data = 361527

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
    
    def __add__(self, c):
        return Cell(self.x + c.x, self.y + c.y)

    def dist(self):
        return abs(self.x) + abs(self.y)

def count_around(n):
    print "Counting to", n
    total = 1
    ring = 1
    pos = [0, 0]
    directions = [Cell(0, 1), Cell(-1, 0), Cell(0, -1), Cell(1, 0)]
    while total < n:
        pos = Cell(ring, -ring)
        # start of a new ring
        size = ring * 2 + 1
        for d in directions:
            for i in xrange(size - 1):
                pos = pos + d
                total += 1
                if total == n: break
            if total == n: break
        ring += 1
    return pos

print "Part 1:"
cell = count_around(data)
print "Value in:", cell
print "Manattan dist:", cell.dist()

def count_around2(n):
    print "Counting to", n
    pos = Cell(0, 0)
    cells = {(0, 0):1}
    last = 1
    ring = 1
    directions = [Cell(0, 1), Cell(-1, 0), Cell(0, -1), Cell(1, 0)]
    def get_value(x, y):
        if (cells.has_key((x, y))):
            return cells[(x, y)]
        else:
            return 0
    while True:
        pos = Cell(ring, -ring)
        size = ring * 2 + 1
        for d in directions:
            for i in xrange(size - 1):
                pos = pos + d
                val = 0
                for x in xrange(pos.x - 1, pos.x + 2):
                    for y in xrange(pos.y - 1, pos.y + 2):
                        val += get_value(x, y)
                if val > n:
                    return val
                cells[(pos.x, pos.y)] = val
        ring += 1

print "\nPart 2"
print count_around2(data)
    