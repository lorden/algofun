"""
Define a data structure that supports push, pop, and min in O(1)
min returns the smallest element in the list
"""
class StackMin:
    items = []
    mins = []

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]
        return None

    def min(self):
        if self.mins:
            return self.mins[len(self.mins) - 1]
        return None

    def push(self, item):
        if not self.min() or self.min() > item:
            self.mins.append(item)
        self.items.append(item)

    def pop(self):
        item = self.peek()
        self.items = self.items[:len(self.items) - 1]
        if item == self.min():
            print 'pop from min'
            self.mins = self.mins[:len(self.mins) - 1]
        return item

    def __repr__(self):
        return "StackMin\nItems: %s\nMins: %s" % (self.items, self.mins)


sm = StackMin()
sm.push(3)
sm.push(5)
sm.push(1)
sm.push(7)
sm.push(2)
print sm
print "Popped: %s" % sm.pop()
print sm
print "Popped: %s" % sm.pop()
print sm
print "Popped: %s" % sm.pop()
print sm
