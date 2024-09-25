def criate_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

duplicate = criate_multiplier(int(input('Enter the multiplier: ')))
print(duplicate(int(input('Enter the value: '))))