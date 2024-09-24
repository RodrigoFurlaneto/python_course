number_str = input('Enter a integer number: ')

try:
    number_int = int(number_str)
    is_even_number = number_int % 2
    if is_even_number == 0:
        print(f'The number {number_int} is a even number')
    else:
        print(f'The number {number_int} is a odd number')
except:
    print("You didn't enter with a integer number!")
