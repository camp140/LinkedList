class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def setData(self, data):
        self.data = data


class List:
    def __init__(self, head=None):
        if head is None:
            self.head = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:
                t = t.next
                self.size += 1

    def __str__(self):
        output = ''
        t = self.head
        while t is not None:
            output += t.data + ' '
            t = t.next
        return output

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1

    def addHead(self, data):
        p = Node(data)
        p.setNext(self.head)
        self.head = p
        self.size += 1

    def isIn(self, data):
        t = self.head
        while t.next is not None:
            if data == t.data:
                return True
            t = t.next
        return False

    def before(self, data):
        if data == self.head:
            return "No Element Before"
        t = self.head
        while t.next is not None:
            if data == t.next.data:
                return t
            t = t.next

    def remove(self, data):
        t = self.head
        while t is not None:
            if data == t.data:
                if self.before(data).next == data:
                    self.before(data).next = None
                else:
                    self.before(data).next = t.next
                self.size -= 1
                return t.data
            t = t.next
        return "No Element"

    def removeTail(self):
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        self.remove(tail.data)
        return tail.data

    def removeHead(self):
        first = self.head
        self.head = self.head.next
        self.size -= 1
        return first.data


def bottomUp(List, percent):
    index = (percent * List.size) // 100
    for i in range(index):
        List.append(List.removeHead())


def deBottomUp(List, percent):
    index = (percent * List.size) // 100
    for i in range(index):
        List.addHead(List.removeTail())


def riffleShuffle(List, percent):
    separate = (percent * List.size) // 100
    insertTime = ((100 - percent) * List.size) // 100
    if percent < 50: insertTime = separate - 1

    t1 = List.head
    t2 = List.head
    for i in range(separate):
        t2 = t2.next

    if percent >= 50:
        tail = List.head
        for i in range(separate - 1):
            tail = tail.next
        tail.next = None

    for i in range(insertTime):
        temp1 = t1.next
        temp2 = t2.next
        t1.next = t2
        t2.next = temp1
        t1 = temp1
        t2 = temp2

    if percent < 50: t1.next = t2


def deRiffle(List, percent):
    separate = (percent * List.size) // 100

    t1 = List.head
    t2 = t1.next
    temp = t2

    if separate == 0 or separate == 10:
        return List

    elif separate < 5:
        for i in range(separate - 1):
            t1.next = t1.next.next
            t2.next = t2.next.next
            t1 = t1.next
            t2 = t2.next
        t2.next = t1.next.next
        t2 = t2.next
        while t2.next is not None:  #go to last
            t2 = t2.next
        t1.next = temp
        t2.next = None
    else:
        for i in range(9 - separate):
            t1.next = t1.next.next
            t2.next = t2.next.next
            t1 = t1.next
            t2 = t2.next
        if t1.next.next is not None:
            t1.next = t1.next.next
            t1 = t1.next
            while t1.next is not None:  #go to last
                t1 = t1.next
            t1.next = temp
            t2.next = None
        else:
            t1.next = temp
            t2.next = None

# tail = Node('D')
# n3 = Node('C', tail)
# n2 = Node('B', n3)
# head = Node('A', n2)
#
# l = List(head)
# print(l)
# print(f'size: {l.getSize()}')
# print(f'Empty?: {l.isEmpty()}')
# l.append('E')
# print(l)
# print(f'size: {l.getSize()}')
# l.addHead('0')
# print(l)
# print(f'size: {l.getSize()}')
# print(f"is B in list?: {l.isIn('B')}")
# print(f"before C: {l.before('C')}")
# print(f"remove: {l.remove('C')}")
# print(l)
# print(f'size: {l.getSize()}')
# print(f'remove head: {l.removeHead()}')
# print(l)
# print(f'size: {l.getSize()}')
# print(f'remove tail: {l.removeTail()}')
# print(l)
# print(f'size: {l.getSize()}')
n10 = Node('10')
n9 = Node('9', n10)
n8 = Node('8', n9)
n7 = Node('7', n8)
n6 = Node('6', n7)
n5 = Node('5', n6)
n4 = Node('4', n5)
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('1', n2)

l = List(n1)

print(l)

percent = int(input("% input: "))
bottomUp(l, percent)
print(f'Bottom Up: {l}')
deBottomUp(l, percent)
print(f'DeBottom Up: {l}')
percent = int(input("% input: "))
riffleShuffle(l, percent)
print(f'riffleShuffle: {l}')
percent = int(input("% input: "))
deRiffle(l, percent)
print(f'deRiffle: {l}')
