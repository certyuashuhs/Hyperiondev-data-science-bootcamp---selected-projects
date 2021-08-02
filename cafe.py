
menu = ["apple", "orange", "banana", "flower", "sweet"]
stock = {"apple" : 3, "orange" : 4, "banana" : 6, "flower" : 8, "sweet" : 6}
price = {"apple" : 5.50, "orange" : 9.20, "banana" : 4.30, "flower" : 5.60, "sweet" : 6.75}

def remaining_product(lis1, dict1, dict2):
    
    total_stock = 0
    total_value = 0
    i = 0
    
    # iterating through each menu item in the list and getting corresponfing values (for each key) from the  price and stock dictionaries
    for item in lis1:
        print(f'Your remaining {item}s are {dict1[item]} and the value of remaining {item}s is: R{dict1[item] * dict2[item]:.2f}')
        total_stock += stock[menu[i]]
        total_value += (price[menu[i]] * stock[menu[i]])
        i += 1
        
    print(f'total remaining stock of all items: {total_stock}')
    print(f'total value of remaining stock: R{total_value:.2f}')
    
# executing the function with the menu list and stock and price dictionaries
remaining_product(menu, stock, price)
