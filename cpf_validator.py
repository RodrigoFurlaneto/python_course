#this program will validate a CPF

#entering the CPF
cpf = input('Enter a new CPF: ')
nine_cpf_numbers = cpf[:9]

#logic for the first digit
multiplier_first = 10
amount = 0
for digits in nine_cpf_numbers:
    amount += int(digits) * multiplier_first
    multiplier_first -= 1
amount *= 10

remainder = amount % 11
first_digit = 0 if remainder > 9 else remainder

#logic for the secound digit
multiplier_secound = 11
ten_cpf_numbers = cpf[:10]

amount = 0
for digits in ten_cpf_numbers:
    amount += int(digits) * multiplier_secound
    multiplier_secound -= 1
amount *= 10

remainder = amount % 11
secound_digit = 0 if remainder > 9 else remainder

if first_digit == int(cpf[-2]) and secound_digit == int(cpf[-1]):
    print('CPF valid')
else:
    print('CPF invalid')