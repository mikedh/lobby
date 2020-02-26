import lobby

def test_book():

    # Create a LOB object
    lob = lobby.OrderBook()

    ########### Limit Orders #############
    # Create some limit orders
    someOrders = [{'type': 'limit',
                   'side': 'ask',
                   'qty': 5,
                   'price': 101,
                   'tid': 100},
                  {'type': 'limit',
                   'side': 'ask',
                   'qty': 5,
                   'price': 103,
                   'tid': 101},
                  {'type': 'limit',
                   'side': 'ask',
                   'qty': 5,
                   'price': 101,
                   'tid': 102},
                  {'type': 'limit',
                   'side': 'ask',
                   'qty': 5,
                   'price': 101,
                   'tid': 103},
                  {'type': 'limit',
                   'side': 'bid',
                   'qty': 5,
                   'price': 99,
                   'tid': 100},
                  {'type': 'limit',
                   'side': 'bid',
                   'qty': 5,
                   'price': 98,
                   'tid': 101},
                  {'type': 'limit',
                   'side': 'bid',
                   'qty': 5,
                   'price': 99,
                   'tid': 102},
                  {'type': 'limit',
                   'side': 'bid',
                   'qty': 5,
                   'price': 97,
                   'tid': 103},
                  ]
    # Add orders to LOB
    for order in someOrders:
        trades, idNum = lob.processOrder(order, False, False)

if __name__ == '__main__':
    test_book()
