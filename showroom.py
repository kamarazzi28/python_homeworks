class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    for car in cars:
        add(car)


def add(car):
    global db
    if db.head is None:
        db.head = Node(None, None, car)
    elif db.head.data.price > car.price:
        old_head = db.head
        db.head = Node(old_head, None, car)
    else:
        ongoing_node = db.head
        ongoing_next_node = db.head.nextNode

        while True:
            if ongoing_node.nextNode is None:
                ongoing_node.nextNode = Node(None, ongoing_node, car)
                break
            elif ongoing_next_node.data.price > car.price:
                ongoing_node.nextNode = Node(ongoing_next_node, ongoing_node, car)
                ongoing_next_node.prevNode = Node(ongoing_next_node, ongoing_node, car)
                break
            else:
                ongoing_node = ongoing_node.nextNode
                ongoing_next_node = ongoing_next_node.nextNode


def updateName(identification, name):
    ongoing_node = db.head
    while ongoing_node is not None:
        if ongoing_node.data.identification == identification:
            ongoing_node.data.name = name
            break
        else:
            ongoing_node = ongoing_node.nextNode
    return None


def updateBrand(identification, brand):
    ongoing_node = db.head
    while ongoing_node is not None:
        if ongoing_node.data.identification == identification:
            ongoing_node.data.brand = brand
            break
        else:
            ongoing_node = ongoing_node.nextNode
    return None


def activateCar(identification):
    ongoing_node = db.head
    while ongoing_node is not None:
        if ongoing_node.data.identification == identification:
            ongoing_node.data.active = True
            break
        else:
            ongoing_node = ongoing_node.nextNode
    return None


def deactivateCar(identification):
    ongoing_node = db.head
    while ongoing_node is not None:
        if ongoing_node.data.identification == identification:
            ongoing_node.data.active = False
            break
        else:
            ongoing_node = ongoing_node.nextNode
    return None


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    total_price = 0
    ongoing_node = db.head
    while ongoing_node is not None:
        if ongoing_node.data.active:
            total_price += ongoing_node.data.price
        if ongoing_node.nextNode is None:
            return total_price
        ongoing_node = ongoing_node.nextNode


def clean():
    global db
    db = LinkedList()
