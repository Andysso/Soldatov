import random
m = list()

for i in range(random.randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

symm = 0
proisv = 1

for i in range(len(m)):
    symm += m[i]
    proisv *= m[i]

print('Сумма элементов массива:',symm,'\n','Произведение элементов массива:',proisv)
