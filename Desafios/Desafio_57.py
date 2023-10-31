gender = 'S'

while gender != 'M' and gender != 'F':
    print('Please just F or M')
    gender = str(input('What is your gender? '))
    gender = gender.upper()