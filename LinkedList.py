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
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:
                t = t.next
                self.size += 1
            self.tail = t

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
            self.tail = t.next
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
        if data == self.head:
            return self.removeHead()
        elif data == self.tail:
            return self.removeTail()
        while t.next is not None:
            if data == t.data:
                self.before(data).next = t.next
                self.size -= 1
                return t.data
            t = t.next
        return "No Element"

    def removeTail(self):
        last = self.tail
        self.before(self.tail.data).next = None
        self.tail = self.before(self.tail.data)
        self.size -= 1
        return last

    def removeHead(self):
        first = self.head
        self.head = self.head.next
        self.size -= 1
        return first


tail = Node('D')
n3 = Node('C', tail)
n2 = Node('B', n3)
head = Node('A', n2)

l = List(head)
print(l)
print(f'tail: {l.tail}')
print(l.getSize())
print(l.isEmpty())
l.append('E')
print(l)
print(f'tail: {l.tail}')
print(l.getSize())
l.addHead('0')
print(l)
print(l.getSize())
print(l.isIn('B'))
print(l.before('C'))
print(l.remove('C'))
print(l)
print(l.getSize())
print(l.removeHead())
print(l)
print(l.removeTail())
print(l)
print(l.getSize())
