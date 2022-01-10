import sqlite3
import atexit
import sys
from DTO import Hat, Supplier, Order
from Repository import repo

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    repo.create_tables()
    id = 1
    ##output = open('output.txt', 'w')
    output = open(str(sys.argv[2]), 'w')

    ## parsing config
    ##file = open('config.txt', 'r')
    file = open(str(sys.argv[0]), 'r')
    data = file.readline()
    amount = data.split(',')
    hats_amount = amount[0]
    suppliers_amount = amount[1]
    list = list()
    for i in range(int(hats_amount)):
        this_hat = file.readline()
        hat_data = this_hat.split(',')
        list.append(Hat(hat_data[0], hat_data[1], hat_data[2], hat_data[3]))

    for i in range(int(suppliers_amount)):
        this_supplier = file.readline()
        supplier_data = this_supplier.split(',')
        repo.suppliers.insert(Supplier(supplier_data[0], supplier_data[1].strip()))

    for hat in list:
        repo.hats.insert(hat)

    ##parsing order, each order, try to make the order

    ##order_txt = open('orders.txt', 'r')
    order_txt = open(str(sys.argv[1]), 'r')
    for line in order_txt:
        order_data = line.split(',')
        topping = order_data[1]
        ##print(topping[:-1])
        true = topping.strip()
        hat = repo.hats.find(true)
        if hat != None:
            repo.orders.insert(Order(id, order_data[0], hat.id))
            supplier = repo.suppliers.find(hat.supplier)
            output.write(true + "," + supplier.name + "," + order_data[0])
            output.write('\n')
            id = id + 1
            ##need to write to txt file, need to get supplier
            if hat.quantity > 1:
                repo.hats.update(hat)
            elif hat.quantity == 1:
                repo.hats.remove(hat)
