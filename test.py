def mult(list):

    total = 1

    for num in list:
        total *= num
    
    print(total)
    return total

def rest(number):
    return "even" if (number%2==0) else "odd"

number_of_user = []
counter=0
while True:
    counter +=1
    number_of_user.append(int(input('enter a number: ')))
    if counter == 4:
        break

rest_value = mult(number_of_user)
print(rest(rest_value))