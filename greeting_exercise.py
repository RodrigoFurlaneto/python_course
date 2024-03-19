user_time = input('Enter the hour: ')

try:
    greeting = int(user_time)

    if greeting >= 0 and greeting < 12:
        print('Good morning!')
    elif greeting < 18:
        print('Good afternoon!')
    elif greeting < 24:
        print('Good evening!')
    else:
        print('You need to enter a value between 0 - 23')
except:
    print('You need to enter a value between 0 - 23')