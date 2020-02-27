"""
order.py
--------------

Handle orders.
"""


class Order(object):
    def __init__(self, quote, orderList):
        self.timestamp = int(quote['timestamp'])
        self.qty = int(quote['qty'])
        self.price = quote['price']
        self.idNum = quote['idNum']
        self.tid = quote['tid']
        self.nextOrder = None
        self.prevOrder = None
        self.orderList = orderList

    def nextOrder(self):
        return self.nextOrder

    def prevOrder(self):
        return self.prevOrder

    def updateQty(self, newQty, newTimestamp):
        if newQty > self.qty and self.orderList.tailOrder != self:
            # Move order to end of the tier (loses time priority)
            self.orderList.moveTail(self)
        self.orderList.volume -= self.qty - newQty
        self.timestamp = newTimestamp
        self.qty = newQty

    def __str__(self):
        return "%s\t@\t%d\tt=%d" % (self.qty, self.price, self.timestamp)
