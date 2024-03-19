import os

shopping_list = []

while True:
    print('Select an option:')
    option = input('[i]nset [d]elete [l]ist: ')
    os.system('cls')
    if option == 'i':
        product = input('Product: ')
        shopping_list.append(product)
        os.system('cls')
    elif option == 'd':
        try:
            item_number = int(input('Item number: '))
            
            del shopping_list[item_number]
        except :
            print('Unable to delete this item!')
    elif option == 'l':
        for index, product in enumerate(shopping_list):
            print(index, product)
    else:
        print("This option doesn't exist. Please, enter a new one!")
    print()