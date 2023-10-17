total = 0
old_man = ''
young_lady = ''
age = 0

for i in range(4):
    name = str(input('Name: '))
    age = int(input('Age: '))
    gender = str(input('Gender: '))
    if age > age and gender == 'male':
        old_man = name
    if age < 20 and gender == 'female':
        young_lady = name
    total += age

print('Average: {}'.format(total / 4))
print('Old man: {}'.format(old_man))
print('Young lady: {}'.format(young_lady))