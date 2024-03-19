first_name = input('Enter your first name: ')

if not first_name.isdigit():
    name_size = len(first_name)
    if name_size < 5:
        print(f'{first_name}, your name is small')
    elif name_size < 7:
        print(f'{first_name}, your name is normal')
    else:
        print(f'{first_name}, your name is big')
else:
    print('You need to enter a string!')