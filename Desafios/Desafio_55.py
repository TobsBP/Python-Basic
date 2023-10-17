less_weight = 9999999
more_wieght = 0

for i in range(0,5):
    weight = int(input('Enter your weight: '))

    if weight > more_wieght:
        more_wieght = weight
    elif weight < less_weight:
        less_weight = weight

print(more_wieght)
print(less_weight)