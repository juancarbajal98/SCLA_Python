def take_order(name):
    print ('Welcome', name, ', what would you like to order?')
    customer_order = input()
    print ('Repeating your order:', customer_order)
    print ('Does this look correct? (y/n)')
    confirm_order = input()
    if confirm_order == 'y':
        exit()
    else:
        take_order(name)


print("Hello, I will be your waiter for today. What is your name? ")

customer_name = input()

take_order(customer_name)