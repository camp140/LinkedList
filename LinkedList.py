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

    def size(self):
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

    def addHead(self, data):
        p = Node(data)
        p.setNext(self.head)
        self.head = p

    def isIn(self, data):
        t = self.head
        while t.next is not None:
            if data == t:
                return True
            t = t.next
        return False

    def before(self, data):
        if self.isIn(data) == True:


n4 = Node('D')
n3 = Node('C', n4)
n2 = Node('B', n3)
n1 = Node('A', n2)

p = n1
while p is not None:
    print(p, end=' ')
    p = p.next
