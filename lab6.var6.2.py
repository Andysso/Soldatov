m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

symm = 0

for i in range(len(m)):
    if m[i] > 5:
        symm += m[i]
print('Сумма чисел, которые больше "5":',symm)
