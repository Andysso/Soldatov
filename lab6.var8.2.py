import random
m = list()
cr_arifm = 0

for i in range(random.randint(5,10)):
    print('Введите',i+1,' элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    cr_arifm += m[i]

cr_arifm /= len(m)

for i in range(len(m)):
    if m[i] == 0:
        m[i] = cr_arifm

print('Полученныый массив:\n',m)
